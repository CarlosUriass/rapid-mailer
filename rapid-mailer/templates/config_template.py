import os
from dotenv import load_dotenv

# Carga el archivo .env en las variables de entorno
load_dotenv()

RESEND_API_KEY = os.getenv("RESEND_API_KEY")
EMAIL_SENDER = os.getenv("EMAIL_SENDER")