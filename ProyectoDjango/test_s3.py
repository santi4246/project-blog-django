import os
from pathlib import Path
import boto3
from botocore.exceptions import ClientError
import environ

# Directorio Base
BASE_DIR = Path(__file__).resolve().parent

# Leer variables del .env
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))
env = environ.Env(
    DEBUG=(bool, False),
    DB_CONN_MAX_AGE=(int, 0),
    DJANGO_ENV=(str, "development")  # development / production
)

# Credenciales y bucket
AWS_ACCESS_KEY_ID = env("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = env("AWS_SECRET_ACCESS_KEY")
AWS_S3_BUCKET_NAME = env("AWS_STORAGE_BUCKET_NAME")
AWS_REGION = env("AWS_S3_REGION_NAME")

# Inicializar cliente S3
s3 = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=AWS_REGION
)

# Archivo de prueba (puede ser cualquier archivo pequeño)
local_file = "test.txt"
with open(local_file, "w") as f:
    f.write("Prueba de PutObject en S3")

# Intentar subir al bucket
try:
    s3.put_object(
        Bucket=AWS_S3_BUCKET_NAME,
        Key="media/test.txt",  # ruta dentro del bucket
        Body=open(local_file, "rb")
    )
    print("✅ Archivo subido correctamente a S3")
except ClientError as e:
    print("❌ Error al subir:", e)