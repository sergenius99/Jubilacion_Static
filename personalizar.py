"""Sustituye los marcadores de la página de inicio por tus datos reales.

Uso:
    python personalizar.py
o, sin preguntas:
    python personalizar.py midominio.com "Mi Calculadora" "Tu Nombre" tu@email.com

Cambia estos marcadores en index.html, robots.txt y sitemap.xml:
    TU-DOMINIO.com        -> tu dominio (sin https:// ni www)
    NOMBRE-HERRAMIENTA    -> el nombre de la calculadora
    TU-NOMBRE             -> tu nombre o razón social
    TU-EMAIL              -> tu email de contacto
Ejecútalo una sola vez (los marcadores desaparecen al sustituirlos).
"""
import re
import sys
from pathlib import Path

ARCHIVOS = ["index.html", "robots.txt", "sitemap.xml"]
PROHIBIDOS = '<>"&\\'


def pedir(texto, valor):
    valor = valor if valor is not None else input(texto).strip()
    if not valor:
        sys.exit("No puede quedar vacío.")
    if any(c in valor for c in PROHIBIDOS):
        sys.exit(f"Evita estos caracteres: {PROHIBIDOS}")
    return valor


def main():
    a = sys.argv[1:]
    dominio = pedir("Dominio (por ejemplo midominio.com): ", a[0] if len(a) > 0 else None)
    nombre = pedir("Nombre de la calculadora: ", a[1] if len(a) > 1 else None)
    titular = pedir("Tu nombre o razón social: ", a[2] if len(a) > 2 else None)
    email = pedir("Tu email de contacto: ", a[3] if len(a) > 3 else None)

    dominio = re.sub(r"^https?://", "", dominio).strip("/")
    if dominio.startswith("www."):
        dominio = dominio[4:]
    if "." not in dominio or " " in dominio:
        sys.exit("El dominio no parece válido (ejemplo: midominio.com).")

    carpeta = Path(__file__).parent
    for nombre_archivo in ARCHIVOS:
        ruta = carpeta / nombre_archivo
        texto = ruta.read_text(encoding="utf-8")
        texto = (texto.replace("TU-DOMINIO.com", dominio)
                      .replace("NOMBRE-HERRAMIENTA", nombre)
                      .replace("TU-NOMBRE", titular)
                      .replace("TU-EMAIL", email))
        ruta.write_text(texto, encoding="utf-8")
        print("Actualizado:", nombre_archivo)

    print(f"\nListo. Web: https://{dominio}/   ·   App: https://app.{dominio}/")


if __name__ == "__main__":
    main()
