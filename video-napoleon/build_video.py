#!/usr/bin/env python3
"""Genera el video MP4 estilo History Matters: ¿Por qué Napoleón no se detuvo?"""
import subprocess, os, sys, math, textwrap
from PIL import Image, ImageDraw, ImageFont

W, H = 1280, 720
FPS = 24
OUT = "video-napoleon/napoleon-video.mp4"
FF = subprocess.check_output(["python3","-c","import imageio_ffmpeg; print(imageio_ffmpeg.get_ffmpeg_exe())"]).decode().strip()

# Duraciones medidas
SCENES = [
    {"audio":"video-napoleon/audio/escena1.mp3","dur":35.51,"title":"ESCENA 1 · EL IMPERIO EN SU CIMA","kicker":"1799 → 1812: Europa redibujada",
     "subs":["En 1799, Europa era un puzzle de reyes que se odiaban.","En 1812, Napoleón había redibujado el mapa.","Prusia vasallo. Austria humillada. España e Italia bajo control francés.","Fun fact: gobernaba a más de 40 millones de personas.","Entonces... ¿por qué no se detuvo?","Porque su imperio necesitaba guerras para sobrevivir."]},
    {"audio":"video-napoleon/audio/escena2.mp3","dur":54.71,"title":"ESCENA 2 · EL OBSTÁCULO: GRAN BRETAÑA","kicker":"El Sistema Continental y sus 3 fracasos",
     "subs":["El problema tenía nombre: Gran Bretaña.","El Canal de la Mancha era un muro de agua.","Invadir Inglaterra era cruzar el océano en bici.","Napoleón prohibió todo comercio británico.","¿Funcionó? No. Por tres razones:","1) Portugal y Rusia hacían trampa en secreto.","2) Contrabando: azúcar y café por mil puertos falsos.","3) Los británicos contra-bloquearon... con barcos."]},
    {"audio":"video-napoleon/audio/escena3.mp3","dur":47.03,"title":"ESCENA 3 · LA PAZ QUE NO DURÓ","kicker":"Amiens 1802 → Austerlitz → Wagram",
     "subs":["La Paz de Amiens (1802) duró apenas un año.","Napoleón anexaba territorios en plena paz.","Para Austria: si hoy es tu vecino, mañana eres tú.","1805: Austerlitz. Victoria perfecta.","¿Paró? No. Pidió más.","1809: Wagram. Y volvió a pedir más.","Cada victoria creaba la siguiente coalición."]},
    {"audio":"video-napoleon/audio/escena4.mp3","dur":41.91,"title":"ESCENA 4 · POR QUÉ NO PODÍA PARAR","kicker":"Personalidad · Vasallos · Miedo ideológico",
     "subs":["Tres motivos. Primero: su personalidad.","Cada tratado era un alto, no un destino.","Segundo: no tenía aliados, tenía vasallos.","Un vasallo te abandona cuando huele derrota.","Tercero: miedo ideológico.","Los reyes temían el contagio revolucionario.","Mejor derrotarlo que contagiarse."]},
    {"audio":"video-napoleon/audio/escena5.mp3","dur":41.59,"title":"ESCENA 5 · OFERTAS RECHAZADAS Y CAÍDA","kicker":"Fráncfort 1813 · Châtillon 1814 · Waterloo 1815",
     "subs":["En 1813 le ofrecieron la paz con fronteras de 1792.","Napoleón dudó... y rechazó.","En 1814, lo mismo. Rechazó otra vez.","Creía que aún podía ganar. No podía.","Waterloo 1815. Abdicación. Santa Elena.","Perdió porque nunca supo cuándo había ganado."]},
]

def font(sz, bold=False):
    paths = ["/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
             "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"]
    for p in paths:
        if os.path.exists(p):
            return ImageFont.truetype(p, sz)
    return ImageFont.load_default()

F_TITLE = font(34, True); F_KICK = font(22); F_LABEL = font(20, True); F_SUB = font(26); F_SMALL = font(18); F_BIG = font(52, True)

# Colores History Matters
PARCH = (242,232,213); SEA = (168,216,234); INK = (30,30,40)
BLUE = (44,90,160); RED = (192,57,43); YELLOW = (230,126,34); GRAY = (150,150,150); GREEN = (39,174,96); PURPLE=(142,68,173)

# Mapa estilizado: (nombre, x, y, w, h, color_base)
MAP = [
    ("GRAN BRETAÑA", 90, 90, 210, 90),
    ("PORTUGAL", 90, 300, 130, 70),
    ("ESPAÑA", 240, 330, 180, 80),
    ("FRANCIA", 300, 210, 200, 90),
    ("PRUSIA", 540, 150, 170, 80),
    ("AUSTRIA", 540, 260, 180, 80),
    ("ITALIA", 420, 400, 150, 90),
    ("RUSIA", 760, 150, 340, 200),
    ("POLONIA", 560, 380, 170, 70),
]

def draw_map(d, t_frac, scene_idx):
    # t_frac 0..1 dentro de la escena
    for i,(name,x,y,w,h) in enumerate(MAP):
        # color según escena y tiempo
        if name=="GRAN BRETAÑA": c = RED
        elif name=="FRANCIA": c = BLUE
        elif name=="RUSIA": c = GREEN if scene_idx<4 else RED
        elif name in ("PRUSIA","AUSTRIA","POLONIA","ITALIA","ESPAÑA","PORTUGAL"):
            # escena 1: azul se expande; escena 5: vuelve a gris/rojo
            if scene_idx==0:
                c = BLUE if t_frac > 0.15 + i*0.05 else GRAY
            elif scene_idx==4:
                c = BLUE if (name=="ESPAÑA" and t_frac<0.3) else (RED if t_frac>0.6 else GRAY)
            else:
                c = BLUE if name in ("ITALIA","ESPAÑA") else GRAY
        else: c = GRAY
        # borde
        d.rounded_rectangle([x,y,x+w,y+h], radius=12, fill=c, outline=INK, width=3)
        # etiqueta
        d.text((x+w/2, y+h/2), name, font=F_LABEL, fill=(255,255,255), anchor="mm")
    # flechas / barcos animados
    if scene_idx==1:  # barcos Royal Navy
        for k in range(3):
            bx = 120 + ((t_frac*400 + k*140) % 500)
            by = 220 + math.sin(t_frac*10+k)*15
            d.polygon([(bx,by),(bx+40,by),(bx+28,by+16),(bx+12,by+16)], fill=INK)
            d.rectangle([bx+14,by-12,bx+26,by], fill=INK)
        d.text((640, 520), "🚢  ROYAL NAVY: el muro de agua", font=F_SMALL, fill=INK, anchor="mm")
    if scene_idx==2:  # ciclo
        # flecha circular
        cx, cy, r = 640, 300, 90
        d.arc([cx-r,cy-r,cx+r,cy+r], start=0, end=360, fill=RED, width=6)
        a = t_frac*360
        ax = cx + r*math.cos(math.radians(a)); ay = cy + r*math.sin(math.radians(a))
        d.ellipse([ax-10,ay-10,ax+10,ay+10], fill=RED)
        d.text((640, 520), "GANAR → ANEXAR → PROVOCAR → GANAR OTRA VEZ", font=F_SMALL, fill=INK, anchor="mm")
    if scene_idx==0 and t_frac>0.5:
        d.text((640, 520), "40+ millones bajo control francés", font=F_SMALL, fill=INK, anchor="mm")
    if scene_idx==4 and t_frac>0.7:
        # Santa Elena
        d.ellipse([1080,520,1120,560], fill=RED, outline=INK, width=3)
        d.text((1100, 580), "SANTA ELENA", font=F_SMALL, fill=INK, anchor="mm")

def draw_frame(scene_idx, t):
    sc = SCENES[scene_idx]
    frac = t / sc["dur"]
    img = Image.new("RGB", (W,H), PARCH)
    d = ImageDraw.Draw(img)
    # mar
    d.rectangle([0,0,W,120], fill=SEA)
    # título
    d.text((40, 30), sc["title"], font=F_TITLE, fill=INK)
    d.text((40, 78), sc["kicker"], font=F_KICK, fill=(80,80,80))
    d.text((W-40, 40), f"{scene_idx+1} / 5", font=F_SMALL, fill=INK, anchor="ra")
    # mapa
    draw_map(d, frac, scene_idx)
    # subtítulo (reparto proporcional)
    n = len(sc["subs"]); idx = min(n-1, int(frac*n))
    sub = sc["subs"][idx]
    # caja subtítulo
    d.rounded_rectangle([60, H-130, W-60, H-50], radius=14, fill=(20,20,30))
    # wrap
    lines = textwrap.wrap(sub, width=62)
    for j,ln in enumerate(lines[:2]):
        d.text((W/2, H-105+j*32), ln, font=F_SUB, fill=(255,255,255), anchor="mm")
    # barra progreso global
    total = sum(s["dur"] for s in SCENES)
    done = sum(s["dur"] for s in SCENES[:scene_idx]) + t
    d.rectangle([0, H-8, W, H], fill=(200,200,200))
    d.rectangle([0, H-8, W*(done/total), H], fill=RED)
    # marca "HISTORY MATTERS · NAPOLEÓN"
    d.text((W/2, 12), "HISTORY MATTERS  ·  ¿POR QUÉ NAPOLEÓN NO SE DETUVO?", font=F_SMALL, fill=INK, anchor="ma")
    return img

def main():
    os.makedirs("video-napoleon/frames", exist_ok=True)
    # concat audio
    print("Concatenando audio...")
    concat_list = "video-napoleon/concat.txt"
    with open(concat_list,"w") as f:
        for s in SCENES:
            f.write(f"file '{os.path.abspath(s['audio'])}'\n")
    subprocess.run([FF,"-y","-f","concat","-safe","0","-i",concat_list,"-c","copy","video-napoleon/audio-full.mp3"], check=True)
    total = sum(s["dur"] for s in SCENES)
    nframes = int(total*FPS)
    print(f"Total {total:.1f}s, frames {nframes}")
    cmd = [FF,"-y","-f","rawvideo","-pix_fmt","rgb24","-s",f"{W}x{H}","-r",str(FPS),"-i","-",
           "-i","video-napoleon/audio-full.mp3","-c:v","libx264","-pix_fmt","yuv420p","-c:a","aac","-b:a","128k",
           "-shortest", OUT]
    proc = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    # tiempos acumulados
    bounds=[]; acc=0
    for s in SCENES:
        bounds.append((acc, acc+s["dur"])); acc+=s["dur"]
    for fi in range(nframes):
        t = fi/FPS
        # escena actual
        si = 0
        for i,(a,b) in enumerate(bounds):
            if t < b: si=i; break
        else: si=len(bounds)-1
        local = t - bounds[si][0]
        img = draw_frame(si, local)
        proc.stdin.write(img.tobytes())
        if fi%240==0: print(f"frame {fi}/{nframes} t={t:.1f}s escena {si+1}", flush=True)
    proc.stdin.close(); proc.wait()
    print("OK:", OUT)

if __name__=="__main__":
    main()
