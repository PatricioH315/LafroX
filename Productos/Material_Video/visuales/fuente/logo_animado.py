"""Animación del logotipo oficial LafroX (Escena 1, 0:00–0:04): MP4 1920x1080, 30 fps, H.264, ~12 Mbps.

Usa el isotipo oficial (lafrox-isotipo.svg del sitio lafrox.github.io) y las tipografías Archivo e IBM Plex Mono (OFL).
Uso:  python logo_animado.py [ruta_ffmpeg]
Requisitos: Pillow y ffmpeg (en el PATH, como argumento o vía el paquete imageio-ffmpeg).
"""
import os, re, sys, shutil, subprocess
from PIL import Image, ImageDraw, ImageFont, ImageChops
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import lafrox_brand as B

W, H, FPS, DUR, SS = 1920, 1080, 30, 4.0, 2
ISO = 260                     # alto del isotipo en px (1x)
OUT = os.path.normpath(os.path.join(B.AQUI, "..", "video", "E1_logo_animado.mp4"))


def rgb(h): h = h.lstrip("#"); return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))
def ease(t): t = max(0.0, min(1.0, t)); return 1 - (1 - t) ** 3
def ease_back(t):
    t = max(0.0, min(1.0, t)); c = 1.4; return 1 + (c + 1) * (t - 1) ** 3 + c * (t - 1) ** 2


def ffmpeg_bin():
    if len(sys.argv) > 1: return sys.argv[1]
    if shutil.which("ffmpeg"): return shutil.which("ffmpeg")
    try:
        import imageio_ffmpeg; return imageio_ffmpeg.get_ffmpeg_exe()
    except ImportError:
        sys.exit("No se encontró ffmpeg. Instálelo o pase su ruta como argumento.")


def iso_mask(size):
    """Máscara del isotipo (regla par-impar sobre los subtrayectos M…Z del SVG oficial)."""
    s = size / B.ISO_VB
    m = Image.new("L", (size, size), 0)
    for sub in re.findall(r"M[^M]+", B.ISO_D):
        nums = list(map(float, re.findall(r"-?\d+(?:\.\d+)?", sub)))
        pts = [(nums[i] * s, nums[i + 1] * s) for i in range(0, len(nums) - 1, 2)]
        if len(pts) < 3:
            continue
        layer = Image.new("L", (size, size), 0)
        ImageDraw.Draw(layer).polygon(pts, fill=255)
        m = ImageChops.logical_xor(m.convert("1"), layer.convert("1")).convert("L")
    return m


def fuentes(px):
    fa = ImageFont.truetype(os.path.join(B.FONTS, "Archivo-VF.ttf"), int(px * 0.62))
    fa.set_variation_by_axes([900, 100])
    fm = ImageFont.truetype(os.path.join(B.FONTS, "IBMPlexMono-Medium.ttf"), int(px * 0.19))
    return fa, fm


iso_px = ISO * SS
MASK = iso_mask(iso_px)
FA, FM = fuentes(iso_px)
GAP = int(iso_px * 0.28)
txt_bb = FA.getbbox("LAFROX")
txt_w = txt_bb[2] - txt_bb[0]
sub_lines = ["INGENIERÍA", "LOGÍSTICA"]
spacing = iso_px * 0.19 * 0.14
sub_w = max(sum(FM.getlength(c) + spacing for c in l) for l in sub_lines)
pad_div = int(iso_px * 0.26)
total_w = iso_px + GAP + txt_w + GAP + pad_div + sub_w
X0 = (W * SS - total_w) / 2
Y0 = (H * SS - iso_px) / 2


def draw_spaced(d, xy, text, font, fill, sp):
    x, y = xy
    for ch in text:
        d.text((x, y), ch, font=font, fill=fill); x += font.getlength(ch) + sp


def frame(t):
    img = Image.new("RGB", (W * SS, H * SS), rgb(B.NEGRO))
    # 1) Isotipo: escala con rebote y aparece (0.2–1.0 s)
    p = (t - 0.2) / 0.8
    if p > 0:
        sc = 0.6 + 0.4 * ease_back(p)
        sz = max(2, int(iso_px * sc))
        m = MASK.resize((sz, sz), Image.LANCZOS).point(lambda v: int(v * min(1, ease(p * 1.6))))
        cx, cy = X0 + iso_px / 2, Y0 + iso_px / 2
        img.paste(Image.new("RGB", (sz, sz), rgb(B.ISOTIPO)), (int(cx - sz / 2), int(cy - sz / 2)), m)
    # 2) "LAFROX": barrido de izquierda a derecha (0.9–1.6 s)
    p = ease((t - 0.9) / 0.7)
    tx = X0 + iso_px + GAP
    if p > 0:
        layer = Image.new("L", img.size, 0); d = ImageDraw.Draw(layer)
        ty = Y0 + iso_px / 2 - (txt_bb[1] + txt_bb[3]) / 2
        d.text((tx - txt_bb[0] + (1 - p) * 30 * SS, ty), "LAFROX", font=FA, fill=255)
        clip = Image.new("L", img.size, 0)
        ImageDraw.Draw(clip).rectangle([0, 0, tx + (txt_w + 40 * SS) * p, img.size[1]], fill=255)
        img.paste(Image.new("RGB", img.size, (255, 255, 255)), (0, 0), ImageChops.multiply(layer, clip))
    # 3) Divisor vertical (1.5–1.9 s) y subtítulo (1.8–2.4 s)
    dx = tx + txt_w + GAP
    d = ImageDraw.Draw(img)
    p = ease((t - 1.5) / 0.4)
    if p > 0:
        hh = iso_px * 0.5 * p
        d.rectangle([dx, Y0 + iso_px / 2 - hh / 2, dx + 2 * SS, Y0 + iso_px / 2 + hh / 2], fill=(70, 74, 82))
    p = ease((t - 1.8) / 0.6)
    if p > 0:
        col = tuple(int(c * p + n * (1 - p)) for c, n in zip(rgb(B.TEXTO_TENUE), rgb(B.NEGRO)))
        lh = iso_px * 0.19 * 1.3
        sy = Y0 + iso_px / 2 - lh
        for i, l in enumerate(sub_lines):
            draw_spaced(d, (dx + pad_div, sy + i * lh), l, FM, col, spacing)
    return img.resize((W, H), Image.LANCZOS)


def main():
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    cmd = [ffmpeg_bin(), "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
           "-c:v", "libx264", "-profile:v", "high", "-pix_fmt", "yuv420p", "-r", str(FPS), "-b:v", "12M",
           "-minrate", "12M", "-maxrate", "12M", "-bufsize", "24M", "-x264-params", "nal-hrd=cbr", "-movflags", "+faststart", OUT]
    pr = subprocess.Popen(cmd, stdin=subprocess.PIPE, stderr=subprocess.DEVNULL)
    for i in range(int(DUR * FPS)):
        pr.stdin.write(frame(i / FPS).tobytes())
    pr.stdin.close(); pr.wait()
    frame(DUR).save(OUT.replace(".mp4", "_ultimo_cuadro.png"))
    print("ok", OUT)


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--prueba":
        for t in (0.6, 1.3, 2.0, 4.0):
            frame(t).resize((640, 360)).save(os.path.join(B.AQUI, f"_prueba_{t}.png"))
        print("prueba ok")
    else:
        main()
