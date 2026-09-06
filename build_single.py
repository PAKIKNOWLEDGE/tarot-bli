# -*- coding: utf-8 -*-
"""把 index.html 打包成单文件版：卡图压缩为 640px JPEG 并以 base64 内嵌。"""
import base64, io, re, sys
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).parent
OUT = ROOT / "幻星集塔罗.html"
IMG_RE = re.compile(r"images/([A-Za-z0-9._-]+\.(?:png|jpg))")

def datauri(name: str, width: int = 640, quality: int = 82) -> str:
    im = Image.open(ROOT / "images" / name).convert("RGB")
    if im.width > width:
        im = im.resize((width, round(im.height * width / im.width)), Image.LANCZOS)
    buf = io.BytesIO()
    im.save(buf, "JPEG", quality=quality, optimize=True)
    return "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode()

def main():
    src = (ROOT / "index.html").read_text(encoding="utf-8")
    cache = {}
    total = 0
    def repl(m):
        nonlocal total
        name = m.group(1)
        if name not in cache:
            cache[name] = datauri(name)
            total += 1
            print(f"  embed {name}")
        return cache[name]
    out = IMG_RE.sub(repl, src)
    OUT.write_text(out, encoding="utf-8")
    size = OUT.stat().st_size / 1e6
    print(f"OK: {OUT.name}  {total} images embedded  {size:.2f} MB")

if __name__ == "__main__":
    sys.exit(main())
