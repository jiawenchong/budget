        allowed_raw = os.environ.get("NOTEBOOK_ALLOWED_USERS", "")
        if allowed_raw:
            allowed = {u.strip().lower() for u in allowed_raw.split(",") if u.strip()}
            if username.lower() not in allowed:
                return render_template(
                    "register.html",
                    error="This username is not allowed to register.",
                    username=username,
                ), 403

        first_account = db.count_users() == 0
        user_id = create_account(username, password)
