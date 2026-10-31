# Página de inicio (para que Google tenga algo que indexar)

Una página estática con texto, título y descripción propios que enlaza a la calculadora.
La calculadora (Streamlit) pasa a vivir en un subdominio: `app.tudominio.com`.

## 1. Personalizar
```bash
python personalizar.py
```
Te pregunta dominio, nombre de la calculadora, tu nombre y tu email, y los pone en
`index.html`, `robots.txt` y `sitemap.xml`. Ejecútalo una sola vez.

## 2. Publicar la página en tu dominio (raíz)
Sube estos tres archivos a un repositorio nuevo de GitHub (distinto del de la app) y
publícalo como sitio estático (por ejemplo, un *Static Site* en Render, GitHub Pages o Netlify):
- Sin comando de build.
- Directorio de publicación: la raíz del repositorio (`.`).
- Añade como dominio personalizado `tudominio.com` (y `www.tudominio.com` si quieres).
- En el DNS de tu dominio crea los registros que te indique el servicio.

## 3. Mover la app a un subdominio
En el servicio de Render donde está la calculadora:
1. Quita el dominio raíz (`tudominio.com`) de ese servicio: un dominio solo puede estar en un servicio.
2. Añade `app.tudominio.com` como dominio personalizado.
3. En el DNS crea un registro CNAME `app` apuntando a la dirección `.onrender.com` de la calculadora.

## 4. Google Search Console
1. En «Sitemaps» envía `sitemap.xml`.
2. En «Inspección de URLs» pega `https://tudominio.com/` y pulsa «Solicitar indexación».
3. Pasados unos días busca `site:tudominio.com` en Google.

Si cambias el texto de la página, actualiza `lastmod` en `sitemap.xml`.
