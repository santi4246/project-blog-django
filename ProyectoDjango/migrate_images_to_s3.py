import os
import django
from pathlib import Path
from django.core.files import File
from storages.backends.s3boto3 import S3Boto3Storage

# =========================
# Configurar Django
# =========================
# Ajustá esta ruta según donde esté tu script
BASE_DIR = Path(__file__).resolve().parent

# Definir la configuración del proyecto
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ProyectoDjango.settings")

# Inicializar Django
django.setup()

# =========================
# Importar modelos y storage
# =========================
from Blog.models import Article  # Cambiá si tu modelo está en otra app
s3_storage = S3Boto3Storage()

# =========================
# Carpeta local de media
# =========================
MEDIA_ROOT = BASE_DIR / "media"

# =========================
# Función para subir imágenes
# =========================
def upload_article_images():
    for article in Article.objects.all():
        local_path = MEDIA_ROOT / article.image.name
        if not local_path.exists():
            print(f"[NO EXISTE] {article.image.name}")
            continue

        relative_path = f"media/{article.image.name.replace('\\', '/')}"

        # Subir archivo a S3 con lectura pública
        with open(local_path, "rb") as f:
            s3_storage.save(relative_path, File(f))
            print(f"[OK] Subido a S3 con public-read: {relative_path}")

# =========================
# Ejecutar
# =========================
if __name__ == "__main__":
    upload_article_images()
    print("¡Migración de media completada!")