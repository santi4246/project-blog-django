# 🧾 Checklist de Deploy — Django + AWS S3 + Base de Datos en la Nube

Este documento resume los pasos esenciales para preparar y desplegar una aplicación **Django** en un entorno de producción, utilizando **Render**, **AWS S3** para archivos estáticos y media, y una **base de datos en la nube** (PostgreSQL o MySQL).

---

## ⚙️ 1. Variables de Entorno (`.env`)

Configurar las siguientes variables antes de ejecutar el deploy:

### 🔐 Django
| Variable | Descripción |
|-----------|--------------|
| `SECRET_KEY` | Clave secreta del proyecto Django. |
| `DEBUG` | `False` en producción, `True` en local. |
| `ALLOWED_HOSTS` | Lista de dominios permitidos. Ej: `['tu-dominio.com', 'render-app.onrender.com']` |
| `DJANGO_ENV` | Define el entorno: `"development"` o `"production"`. |

### 🗄️ Base de Datos
| Variable | Descripción |
|-----------|--------------|
| `DB_ENGINE` | Backend de base de datos (ej: `django.db.backends.postgresql`). |
| `DB_NAME` | Nombre de la base de datos. |
| `DB_USER` | Usuario de la base de datos. |
| `DB_PASSWORD` | Contraseña del usuario. |
| `DB_HOST` | Host de la base de datos. |
| `DB_PORT` | Puerto de conexión. |
| `DB_SSL_CA` | Ruta al certificado CA si el proveedor lo requiere (opcional). |
| `DB_CONN_MAX_AGE` | Ej: `600` para conexiones persistentes. |

### ☁️ AWS S3 (solo producción)
| Variable | Descripción |
|-----------|--------------|
| `AWS_ACCESS_KEY_ID` | ID de clave de acceso de AWS. |
| `AWS_SECRET_ACCESS_KEY` | Clave secreta de AWS. |
| `AWS_STORAGE_BUCKET_NAME` | Nombre del bucket S3. |
| `AWS_S3_REGION_NAME` | Región de AWS (ej: `us-east-1`). |

---

## 🧩 2. Base de Datos en la Nube

✅ Verificar que el **firewall** de la base de datos permita conexiones desde:
- La **IP local** (para desarrollo).
- La **IP o VPC de Render** (para producción).

✅ Si el proveedor lo requiere:
- Configurar conexión **SSL** (`DB_SSL_CA`).
- Ajustar `CONN_MAX_AGE` para reducir overhead de conexiones.

✅ Activar **backups automáticos** desde el panel del proveedor.

---

## 🧱 3. Archivos Estáticos y Media

### Estáticos (CSS, JS)
- **Local:** Servidos directamente por Django.
- **Producción:** Usar **Whitenoise** con `CompressedManifestStaticFilesStorage` para mejor rendimiento.

### Media (uploads)
- **Local:** Guardados con `FileSystemStorage` en `/media/`.
- **Producción:** Usar `S3Boto3Storage` con un bucket público o URLs pre-firmadas para mayor seguridad.

📄 Si el bucket es público:
```python
AWS_QUERYSTRING_AUTH = False

🔒 4. Seguridad en Producción

Activar las siguientes configuraciones en settings.py:
HTTPS y cookies seguras
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

HSTS (HTTP Strict Transport Security)
SECURE_HSTS_SECONDS = 3600
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_CONTENT_TYPE_NOSNIFF = True

🧰 Extra: Recomendaciones

* Ejecutar python manage.py collectstatic antes del deploy.
* Usar DEBUG=False siempre en producción.
* Monitorear logs y conexiones desde el dashboard del proveedor (Render, AWS, etc).