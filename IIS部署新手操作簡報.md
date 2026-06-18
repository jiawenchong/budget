# Python (Flask) + IIS 部署新手操作簡報

> 適用情境：把 Flask 網站部署到 **Windows Server + IIS**，用 **HttpPlatformHandler + Waitress**，並支援 **AD Windows 驗證 (SSO)**。
> 本文以實際專案 `budgetagent` 為例（部署路徑 `D:\Web Service\budgetagent`，Port `8001`）。請把路徑/名稱換成你自己的。

---

## 0. 先搞懂三個角色（白話）

| 名詞 | 白話 | 工作 |
|------|------|------|
| **IIS** | 餐廳大門 + 接待員 | 接收瀏覽器請求、做 Windows 身分驗證 |
| **HttpPlatformHandler** | IIS 的外掛 | 自動「啟動你的 Python」、當機自動重開 |
| **Waitress** | 翻譯員 | 把網頁請求翻成 Python 看得懂的格式 |
| **Flask (你的程式)** | 廚師 | 真正做事、回傳網頁 |

**為什麼用這套？**
- 員工免登入（自動認出 Windows 身分 = SSO）
- 程式當掉自動重啟
- 關掉所有視窗、登出、重開機，網站都照跑（IIS 在背景當服務）

---

## 1. ⭐ 最重要觀念：有「兩台電腦」

| 動作 | 在哪台做 | 指令開頭 |
|------|---------|---------|
| **下載打包套件**（產生 wheels） | 🌐 **有網路的電腦** | `pip download` |
| **其他全部**（裝 IIS、venv、設定、上線） | 💻 **部署機** | — |

> 口訣：**只有「下載 wheels」去有網路的電腦，剩下全部都在部署機。**

---

## 2. 事前準備

### 跟 IT / AD 管理員要
- AD 伺服器短名（例 `KH`）、完整網域（例 `kh.asegroup.com`）、BaseDN（例 `DC=kh,DC=asegroup,DC=com`）
- 登入格式（`網域\工號` 或 UPN）
- **對外上網的 Proxy 位址 + Port**（公司內網幾乎都有，下載 wheels 會用到）

### 要下載的三個東西
1. **Python 安裝檔**（python.org，64-bit）
2. **HttpPlatformHandler v2.0 MSI**（iis.net，IIS 不內建，要單獨裝）
3. 你的**專案程式碼**（含 `requirements.txt`）

### 先確認
- 部署路徑、Port、部署機的 **Python 版本**（後面 wheels 要對齊它）

---

## 3. Step 1：部署機安裝環境

### 3-1 裝 IIS（含 Windows 驗證 + CGI）
系統管理員 PowerShell：
```powershell
Install-WindowsFeature -Name Web-Server,Web-Windows-Auth,Web-CGI -IncludeManagementTools
```

### 3-2 裝 HttpPlatformHandler（點兩下 MSI），裝完驗證：
```powershell
Get-WebGlobalModule -Name "httpPlatformHandler"
```
**有輸出 = 成功。沒輸出 = 沒裝好，重裝 MSI。**（這步沒做好，最後會 500.19）

### 3-3 裝 Python（安裝畫面務必勾選）
- ☑ **Install for all users**（必勾，不勾整套會失敗）
- ☑ **Add Python to PATH**

驗證裝在哪：
```powershell
where.exe python
```
要是 `C:\Program Files\Python3X\...`；若在 `AppData` → **重裝**。

---

## 4. Step 2：建 venv + 裝套件

### 4-1 ⭐ 先在「有網路電腦」把 wheels 裝滿（不是手動建空資料夾！）

> 常見坑：手動建一個叫 `wheels` 的空資料夾 → 裡面沒東西 → 部署機裝不起來。

在有網路電腦的專案資料夾：
```powershell
pip download -r requirements.txt -d wheels --platform win_amd64 --python-version 3.14 --only-binary=:all: --proxy "http://工號:密碼@proxy位址:port"
```
- **`--python-version` 要對齊「部署機」的 Python 版本**（本例部署機是 3.14 就寫 3.14）
- **Proxy 407 錯誤** → 加 `--proxy`（位址在「設定 → Proxy」查，或問 IT）
- 密碼有特殊符號要轉碼：`@`→`%40`、`#`→`%23`、`\`→`%5C`
- `--proxy` 整段要在**同一行**，頭尾引號要成對（出現 `>>` 是引號沒閉合，按 `Ctrl+C` 重來）

檢查有沒有裝滿：
```powershell
dir wheels
```
要看到一堆 `.whl`。編譯型套件檔名要對上版本，例如 `psycopg2_binary-...-cp314-cp314-win_amd64.whl`（`cp314` = Python 3.14）。

### 4-2 ⭐ requirements.txt 別漏了 waitress / pywin32

> 真實踩坑：requirements.txt 只寫了 Flask 等，**漏了 `waitress`**（網站靠它跑）和 `pywin32`（AD SSO 讀身分用）。結果 `waitress-serve.exe` 一直不存在。

requirements.txt 至少要有：
```
Flask>=3.0.0
waitress>=3.0.0
pywin32>=306
ldap3>=2.9.1
（+ 你專案其他套件，如 flask-cors / psycopg2-binary / openpyxl / APScheduler...）
```

### 4-3 把整包 wheels 搬到部署機，在部署機建 venv + 離線安裝

> ⭐ venv **必須在部署機重建**，不可從別處複製（否則 `Fatal error in launcher`）。

```powershell
cd "D:\Web Service\budgetagent"
python -m venv venv
.\venv\Scripts\python --version          # 確認版本與 wheels 一致（本例 3.14）
.\venv\Scripts\pip install --no-index --find-links=wheels -r requirements.txt
```
裝完確認 waitress 真的生出來：
```powershell
dir "D:\Web Service\budgetagent\venv\Scripts\waitress-serve.exe"
```

> 💡 `wheels` 裡是 `waitress-....whl`（安裝包）；`waitress-serve.exe` 是 **pip install 後**才在 `venv\Scripts\` 產生的執行檔。沒有它 = 安裝沒成功。

### 4-4 建 logs 資料夾（手動建或指令都行）
```powershell
New-Item -ItemType Directory -Force ".\logs"
```

---

## 5. Step 3：建立 wsgi.py + web.config

> ⭐⭐ **最大踩坑點**：建檔時**只放檔案內容本身**。
> 不要把 PowerShell 的 `@'  ... '@ | Set-Content` 包裝指令一起存進檔案！
> （那會讓 web.config 開頭變成 `@'` 而不是 `<?xml` → IIS 解析失敗 → 500）
> **新手最穩做法：用記事本，貼「純內容」，存檔。**

### 5-1 `backend\wsgi.py`（app.py 在 backend 子資料夾時）
檔案內容**只有這 4 行**：
```python
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from app import app as application
```

### 5-2 `web.config`（放在專案**最外層**，跟 venv/wheels 同一層）
檔案內容**只有這段 XML**（路徑換成你的；注意有空格的路徑照填，不要折行）：
```xml
<?xml version="1.0" encoding="UTF-8"?>
<configuration>
  <system.webServer>
    <handlers>
      <add name="httpPlatformHandler" path="*" verb="*" modules="httpPlatformHandler" resourceType="Unspecified"/>
    </handlers>
    <httpPlatform processPath="D:\Web Service\budgetagent\venv\Scripts\waitress-serve.exe" arguments="--port=%HTTP_PLATFORM_PORT% --threads=4 wsgi:application" forwardWindowsAuthToken="true" stdoutLogEnabled="true" stdoutLogFile="D:\Web Service\budgetagent\logs\python.log">
      <environmentVariables>
        <environmentVariable name="PYTHONPATH" value="D:\Web Service\budgetagent\backend"/>
        <environmentVariable name="PYTHONUNBUFFERED" value="1"/>
        <environmentVariable name="PYTHONIOENCODING" value="utf-8"/>
      </environmentVariables>
    </httpPlatform>
  </system.webServer>
</configuration>
```
存檔後驗證內容正確（開頭 `<?xml`、結尾 `</configuration>`，沒有 `@'`）：
```powershell
type "D:\Web Service\budgetagent\web.config"
```

> 重點欄位：
> - `processPath` = venv 內 waitress-serve.exe 的**完整正確路徑**
> - `PYTHONPATH` = app.py 所在的資料夾（本例是 `backend`）
> - `forwardWindowsAuthToken="true"` = SSO 必須
> - **不要**在 web.config 放 `<authentication>` 區段（預設被鎖會報錯；改用 IIS 畫面設驗證）

---

## 6. Step 4：建 IIS 網站 + AppPool

### 6-1 建 AppPool（引擎）
IIS 管理員 → 應用程式集區 → 新增：
- 名稱 `Pool-budgetagent`
- **.NET CLR 版本：沒有 Managed 程式碼**
- 進階設定 → **啟動模式：AlwaysRunning**

### 6-2 建網站
IIS 管理員 → **網站**（在「應用程式集區」下方，展開電腦名稱就看得到）→ 新增網站：
- 名稱 `budgetagent`
- 實體路徑 `D:\Web Service\budgetagent`（最外層）
- 應用程式集區選 `Pool-budgetagent`
- Port `8001`

### 6-3 設定驗證
網站 → 中間雙擊「**驗證**」（中間下方要切到「**功能檢視**」才看得到圖示）：
- **匿名驗證 → 停用**
- **Windows 驗證 → 啟用**（提供者確認有 Negotiate / NTLM）

---

## 7. Step 5：⭐ 給 AppPool 帳號資料夾權限

> 真實踩坑：手動跑能開、IIS 跑 500。因為 IIS 用低權限帳號 `IIS AppPool\Pool-budgetagent`，**讀不到程式/venv**。
> UI 設權限在網域環境常卡（「位置」要選**本機電腦**不是網域）。**用 icacls 最穩。**

系統管理員 PowerShell（路徑有空格 → 一定用雙引號）：
```powershell
icacls "D:\Web Service\budgetagent" /grant "IIS AppPool\Pool-budgetagent:(OI)(CI)RX" /T
icacls "D:\Web Service\budgetagent\logs" /grant "IIS AppPool\Pool-budgetagent:(OI)(CI)M" /T
```
看到「已順利處理 N 個檔案」即可。

---

## 8. Step 6：上線測試

```powershell
iisreset
```

### 用「正確的網址」測（不一定是 localhost！）
先看網站綁在哪個 IP：
```powershell
Get-WebBinding
```
- 若是 `*:8001:` → `http://localhost:8001` 可以
- 若是 `10.10.28.170:8001:`（綁特定 IP）→ **要用 `http://10.10.28.170:8001`**（localhost 會 400 Invalid Hostname）

> 想讓 localhost 也能用：把繫結 IP 改成「全部未指派 (All Unassigned)」。

### 出現你的網頁 = 🎉 成功上線
這時可關掉所有視窗、IIS 管理員、甚至登出，網站照跑。

### 讓其他同事連
```powershell
hostname            # 機器名稱
ipconfig            # IPv4
# 開防火牆放行 8001
New-NetFirewallRule -DisplayName "budgetagent-8001" -Direction Inbound -Protocol TCP -LocalPort 8001 -Action Allow
```
同事用 `http://機器名稱:8001` 或 `http://IP:8001` 連；把站台加入瀏覽器「近端內部網路」可避免認證視窗彈出（SSO 用機器名稱比 IP 準）。

---

## 9. 🔧 常見錯誤速查（本次實戰整理）

| 現象 | 原因 | 解法 |
|------|------|------|
| `407 Proxy authentication required` | 公司 proxy 擋 pip | `pip download ... --proxy "http://工號:密碼@位址:port"` |
| PowerShell 出現 `>>` | 引號沒閉合 | `Ctrl+C` 取消，整行重打，頭尾引號成對 |
| `No matching distribution found`（檔案明明在） | wheels 的 cp 版本 ≠ venv 版本 | 用 `python --version` 查 venv，重抓對應 `--python-version` 的 wheels |
| `waitress-serve.exe` 不存在 | requirements.txt 沒寫 waitress / 安裝沒跑完 | 加進 requirements、補裝、重跑 pip install |
| `Fatal error in launcher` | venv 從別處複製來 | 刪 venv，在部署機最終路徑重建 |
| web.config 報「父系鎖定」（authentication） | `<authentication>` 區段預設被鎖 | web.config 拿掉該段，改用 IIS 畫面設驗證 |
| 500（log 沒生成） | web.config 內容錯（含了 `@'`/`Set-Content`） | 用記事本重存「純 XML」 |
| 500（icacls 後仍是） | web.config 內容/格式仍有誤 | `type web.config` 確認開頭是 `<?xml` |
| 500 用 IIS、手動跑卻 OK | AppPool 帳號沒權限 | `icacls` 給 RX（主目錄）/ M（logs） |
| 400 Invalid Hostname | 網站綁特定 IP，用 localhost 連 | 改用該 IP 連，或繫結改「全部未指派」 |
| **500.19 (0x80070021)** 指向 httpPlatformHandler | 模組沒裝，或區段被鎖 | 先 `Get-WebGlobalModule -Name httpPlatformHandler`：沒輸出→重裝 MSI；有輸出→下方解鎖 |
| 502 Bad Gateway | waitress 路徑錯/程式啟動崩潰 | 看 log，檢查 processPath |
| 503 Service Unavailable | AppPool 停了 | IIS 管理員啟動 AppPool |

### 解鎖 httpPlatform 區段（500.19 時）
```powershell
C:\Windows\System32\inetsrv\appcmd.exe unlock config -section:system.webServer/handlers
C:\Windows\System32\inetsrv\appcmd.exe unlock config -section:system.webServer/httpPlatform
iisreset
```

---

## 10. 黃金除錯流程

1. **先手動跑，繞過 IIS**（直接看 Python 真正的錯誤）：
   ```powershell
   cd "D:\Web Service\budgetagent\backend"
   & "D:\Web Service\budgetagent\venv\Scripts\python.exe" -c "import wsgi; print('IMPORT OK')"
   ```
   - 印 Traceback → 程式/套件問題
   - 印 `IMPORT OK` → 程式沒事，問題在 IIS

2. **模擬 IIS 環境手動啟動**：
   ```powershell
   cd "D:\Web Service\budgetagent"
   $env:PYTHONPATH="D:\Web Service\budgetagent\backend"
   & ".\venv\Scripts\waitress-serve.exe" --port=8003 wsgi:application
   ```
   開 `http://localhost:8003`：能開 → 純 IIS 權限/設定問題。

3. **看 IIS 啟動 Python 的失敗紀錄**：
   ```powershell
   Get-WinEvent -LogName Application -MaxEvents 40 |
     Where-Object { $_.Message -like "*HttpPlatform*" -or $_.Message -like "*python*" } |
     Format-List TimeCreated, Message
   ```

4. **看程式 log**：
   ```powershell
   type "D:\Web Service\budgetagent\logs\python.log"
   ```

---

## 速記版流程

```
[有網路電腦] pip download 裝滿 wheels（版本對齊部署機、加 proxy）
        │  USB 搬運
        ▼
[部署機] 裝 IIS + HttpPlatformHandler + Python(for all users)
        → 建 venv(本機重建) → 離線 pip install(含 waitress/pywin32)
        → 寫 wsgi.py + web.config(只放純內容!)
        → IIS 建 AppPool(No Managed/AlwaysRunning) + 網站(實體路徑/Port)
        → 驗證:停匿名/開 Windows
        → icacls 給 AppPool 權限(RX 主目錄 / M logs)
        → iisreset → 用「正確 IP/主機名」開網站
```
