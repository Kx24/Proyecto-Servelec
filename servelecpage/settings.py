from pathlib import Path
import os
from decouple import config

BASE_DIR = Path(__file__).resolve().parent.parent

# ==========================
# Seguridad y modo debug
# ==========================

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY") or config("SECRET_KEY", default=None)

if not SECRET_KEY:
    raise ValueError("SECRET_KEY no está definido. Configúralo en el entorno de producción.")

# DEBUG dinámico
DEBUG = os.environ.get("DEBUG", "False").lower() == "true"

# Hosts permitidos
ALLOWED_HOSTS = ["*"]   
#ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "127.0.0.1,localhost").split(",")
#HTTPS 
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# ==========================
# Archivos estáticos
# ==========================
STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "landingpage" / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"

# WhiteNoise para servir estáticos en producción
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# ==========================
# Aplicaciones
# ==========================
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "landingpage",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "servelecpage.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "Landingpage", "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "servelecpage.wsgi.application"

# ==========================
# Base de datos
# ==========================
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",  # 🔹 reemplazar luego por PostgreSQL en prod
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# ==========================
# Password validation
# ==========================
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# ==========================
# Internacionalización
# ==========================
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# ==========================
# Email
# ==========================
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'  # Para desarrollo, muestra emails en la consola
EMAIL_HOST = "mail.servelec-ingenieria.cl"
EMAIL_PORT = 465
EMAIL_USE_SSL = True
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER") or config("EMAIL_HOST_USER", default="")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD") or config("EMAIL_HOST_PASSWORD", default="")
DEFAULT_FROM_EMAIL = "contacto@servelec-ingenieria.cl"
