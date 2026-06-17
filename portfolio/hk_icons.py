def g(x, y, scale, content):
    return f'<g transform="translate({x},{y}) scale({scale})">{content}</g>'

def teapot(red="#b6312a", gold="#d8a13c"):
    return f'''
    <ellipse cx="0" cy="40" rx="62" ry="40" fill="{red}"/>
    <path d="M -60,30 C -90,10 -90,-20 -55,-15" stroke="{red}" stroke-width="14" fill="none" stroke-linecap="round"/>
    <path d="M 55,5 L 95,-25 L 102,-15 L 65,18 Z" fill="{red}"/>
    <ellipse cx="0" cy="2" rx="40" ry="12" fill="{gold}"/>
    <circle cx="0" cy="-10" r="14" fill="{gold}"/>
    <circle cx="0" cy="-10" r="6" fill="{red}"/>
    '''

def steamer(brown="#c08a4e", dark="#8a5a28"):
    rows = "".join(f'<line x1="-55" y1="{y}" x2="55" y2="{y}" stroke="{dark}" stroke-width="3"/>' for y in range(-30, 31, 12))
    return f'''
    <ellipse cx="0" cy="-32" rx="58" ry="14" fill="{dark}"/>
    <rect x="-55" y="-30" width="110" height="60" rx="8" fill="{brown}"/>
    {rows}
    <ellipse cx="0" cy="30" rx="58" ry="12" fill="{dark}"/>
    '''

def harkau(skin="#fceee0", filling="#e8a06a"):
    pleats = "".join(
        f'<path d="M {x},6 Q {x+9},-22 {x+18},6" stroke="#c89858" stroke-width="2.5" fill="none"/>'
        for x in range(-36, 30, 12)
    )
    return f'''
    <path d="M -40,8 C -40,-22 40,-22 40,8 C 40,26 -40,26 -40,8 Z" fill="{skin}" stroke="#c89858" stroke-width="2.5"/>
    <ellipse cx="0" cy="10" rx="24" ry="10" fill="{filling}"/>
    {pleats}
    '''

def siumai(skin="#f6d978", shrimp="#e0633f"):
    return f'''
    <path d="M -32,10 L -26,-22 L 26,-22 L 32,10 Z" fill="{skin}"/>
    <circle cx="0" cy="-22" r="9" fill="{shrimp}"/>
    <circle cx="-14" cy="6" r="5" fill="#e8a23c"/>
    <circle cx="10" cy="8" r="5" fill="#e8a23c"/>
    '''

def duck(skin="#a8431f", dark="#7a2a12"):
    return f'''
    <path d="M -8,-70 q 14,-8 18,4 l 4,8" fill="none" stroke="{dark}" stroke-width="5" stroke-linecap="round"/>
    <ellipse cx="14" cy="-58" rx="13" ry="11" fill="{skin}"/>
    <path d="M 24,-60 l 14,4 l -14,8 Z" fill="#d8a13c"/>
    <path d="M -34,-44 C -42,-12 -38,30 -10,42 C 14,50 38,30 34,-10 C 30,-40 4,-58 -10,-50 C -22,-44 -30,-50 -34,-44 Z" fill="{skin}"/>
    <path d="M -28,-30 q 30,-10 56,6" fill="none" stroke="{dark}" stroke-width="2" opacity="0.5"/>
    <path d="M -26,0 q 28,-6 54,8" fill="none" stroke="{dark}" stroke-width="2" opacity="0.5"/>
    <path d="M -18,26 q 22,-2 40,10" fill="none" stroke="{dark}" stroke-width="2" opacity="0.5"/>
    <path d="M -2,42 L -10,68" stroke="{dark}" stroke-width="5" stroke-linecap="round"/>
    <path d="M 14,44 L 16,70" stroke="{dark}" stroke-width="5" stroke-linecap="round"/>
    '''

def cheung_fun(roll="#f3ecd8", soy="#5a3318"):
    return f'''
    <ellipse cx="0" cy="14" rx="56" ry="20" fill="#e8dcc0"/>
    <path d="M -48,8 q 96,-22 96,0 q -96,22 -96,0 Z" fill="{roll}" stroke="#d8c89c" stroke-width="2"/>
    <path d="M -40,8 q 80,-12 80,0" fill="none" stroke="#d8c89c" stroke-width="2"/>
    <path d="M -20,18 q 6,8 0,16 M 4,18 q 6,8 0,16 M 26,16 q 6,8 0,16" stroke="{soy}" stroke-width="3" stroke-linecap="round" opacity="0.8"/>
    '''

def turnip_cake(top="#e0b15a", side="#c9893c"):
    return f'''
    <path d="M -42,-4 L 0,-22 L 42,-4 L 42,14 L 0,32 L -42,14 Z" fill="{side}"/>
    <path d="M -42,-4 L 0,-22 L 42,-4 L 0,14 Z" fill="{top}"/>
    <circle cx="-12" cy="-6" r="3.5" fill="#7a4a2e"/>
    <circle cx="10" cy="-10" r="3.5" fill="#c0392b"/>
    <circle cx="-2" cy="2" r="3.5" fill="#7a4a2e"/>
    '''

def char_siu_bowl(rice="#f5ecd2", meat="#9c3a26", bowl="#c0392b"):
    return f'''
    <path d="M -55,0 a 55,30 0 0 0 110,0 Z" fill="{bowl}"/>
    <ellipse cx="0" cy="-4" rx="55" ry="20" fill="{rice}"/>
    <rect x="-30" y="-22" width="22" height="14" rx="4" fill="{meat}" transform="rotate(-10)"/>
    <rect x="-2" y="-26" width="22" height="14" rx="4" fill="{meat}" transform="rotate(8)"/>
    <rect x="14" y="-16" width="20" height="13" rx="4" fill="{meat}" transform="rotate(-5)"/>
    '''

def milk_tea(cup="#f3e3bd", tea="#7a4a2e", saucer="#b6312a"):
    return f'''
    <ellipse cx="0" cy="48" rx="48" ry="10" fill="{saucer}"/>
    <path d="M -32,-30 L -24,40 L 24,40 L 32,-30 Z" fill="{cup}"/>
    <ellipse cx="0" cy="-30" rx="32" ry="9" fill="{tea}"/>
    <path d="M 32,-10 q 26,0 22,22 q -4,16 -26,10" fill="none" stroke="{cup}" stroke-width="8"/>
    '''

def egg_tart(crust="#d8a13c", custard="#f3c14a"):
    return f'''
    <path d="M -40,10 Q -40,-22 0,-22 Q 40,-22 40,10 Z" fill="{crust}"/>
    <path d="M -40,10 Q 0,28 40,10 Q 0,2 -40,10 Z" fill="{crust}"/>
    <ellipse cx="0" cy="-6" rx="30" ry="16" fill="{custard}"/>
    '''

def noodle_bowl(bowl="#b6312a", noodle="#f3d98a", broth="#e8b84a"):
    return f'''
    <path d="M -55,0 a 55,30 0 0 0 110,0 Z" fill="{bowl}"/>
    <ellipse cx="0" cy="-4" rx="55" ry="20" fill="{broth}"/>
    <path d="M -30,-8 q 8,-12 16,0 q 8,-12 16,0 q 8,-12 16,0" stroke="{noodle}" stroke-width="5" fill="none"/>
    <path d="M -25,2 q 8,-12 16,0 q 8,-12 16,0" stroke="{noodle}" stroke-width="5" fill="none"/>
    '''

def bao(skin="#fdf6ea", shadow="#e8dcc0"):
    return f'''
    <ellipse cx="0" cy="26" rx="44" ry="10" fill="{shadow}"/>
    <path d="M -42,18 C -42,-22 42,-22 42,18 C 42,30 -42,30 -42,18 Z" fill="{skin}"/>
    <path d="M -10,-20 q 10,-10 20,0" stroke="#d8c89c" stroke-width="3" fill="none"/>
    <circle cx="0" cy="-20" r="5" fill="#d8c89c"/>
    <path d="M -34,4 q 34,-10 68,0" stroke="{shadow}" stroke-width="2" fill="none" opacity="0.7"/>
    '''

def chopsticks(color="#5a3a22"):
    return f'''
    <rect x="-4" y="-60" width="8" height="120" rx="4" fill="{color}" transform="rotate(8)"/>
    <rect x="10" y="-60" width="8" height="120" rx="4" fill="{color}" transform="rotate(8)"/>
    '''
