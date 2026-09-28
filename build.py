#!/usr/bin/env python3
"""Genera index.html uniendo src/page.html con los retos de src/data.js."""
from pathlib import Path

root = Path(__file__).parent
page = (root / "src/page.html").read_text(encoding="utf-8")
data = (root / "src/data.js").read_text(encoding="utf-8").replace("</script", "<\\/script")
assert page.count("/*__OW_DATA__*/") == 1, "Falta el marcador de datos en src/page.html"
body = page.replace("/*__OW_DATA__*/", data)
html = (
    '<!doctype html>\n<html lang="es">\n<head>\n<meta charset="utf-8">\n'
    '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
    '<style>*,*::before,*::after{box-sizing:border-box}body{margin:0}img{max-width:100%}[hidden]{display:none!important}</style>\n'
    '</head>\n<body>\n' + body + '\n</body>\n</html>\n'
)
(root / "index.html").write_text(html, encoding="utf-8")
print("index.html generado")
