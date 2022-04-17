from .common import *
from django.core.exceptions import ImproperlyConfigured

with open(".secrets.json") as f:
    secrets = json.loads(f.read())


def get_secret(setting, secrets=secrets):
    try:
        return secrets[setting]
    except KeyError:
        error_msg = "Set the {0} environment variable".format(setting)
        raise ImproperlyConfigured(error_msg)


# django-debug-toolbar https://django-debug-toolbar.readthedocs.io/en/latest/
# django-extensions https://django-extensions.readthedocs.io/en/latest/installation_instructions.html
# drf-yasg https://drf-yasg.readthedocs.io/en/stable/readme.html#usage
DEBUG = True
INSTALLED_APPS += [
    "debug_toolbar",
    "django_extensions",
    "drf_yasg",
]
MIDDLEWARE = [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
] + MIDDLEWARE
INTERNAL_IPS = ["127.0.0.1"]

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
]

SWAGGER_SETTINGS = {
    "LOGIN_URL": "/admin/login",
    "USE_SESSION_AUTH": True,
    "SECURITY_DEFINITIONS": {
        # 'Token': {'type': 'apiKey', 'name': 'Authorization', 'in': 'header'}, # 토큰 사용시
        # "basic": {
        #     "type": "basic", # id, password 그러나 셋팅을 바꿔야할듯
        # },
        "JWT": {"type": "apiKey", "name": "Authorization", "in": "header"},
    },
    "JSON_EDITOR": True,
    "SHOW_REQUEST_HEADERS": True,
    "OPERATIONS_SORTER": "alpha",
    "PERSIST_AUTH": True,
}

# AWS
AWS_S3_ACCESS_KEY_ID = get_secret(
    "AWS_S3_ACCESS_KEY_ID"
)  # .csv 파일에 있는 내용을 입력 Access key ID
AWS_S3_SECRET_ACCESS_KEY = get_secret(
    "AWS_S3_SECRET_ACCESS_KEY"
)  # .csv 파일에 있는 내용을 입력 Secret access key

AWS_REGION = "ap-northeast-2"

###S3 Storages
AWS_STORAGE_BUCKET_NAME = get_secret("AWS_STORAGE_BUCKET_NAME")  # 설정한 버킷 이름
AWS_S3_CUSTOM_DOMAIN = "%s.s3.%s.amazonaws.com" % (AWS_STORAGE_BUCKET_NAME, AWS_REGION)
AWS_S3_OBJECT_PARAMETERS = {
    "CacheControl": "max-age=86400",
}
AWS_DEFAULT_ACL = "public-read"
AWS_LOCATION = "static"

STATTIC_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
STATICFILES_STORAGE = "storages.backends.s3boto3.S3StaticStorage"
DEFAULT_FILE_STORAGE = "backend.storages.MediaStorage"


# DATABASE
# Dockerfile error https://stackoverflow.com/questions/59554493/unable-to-fire-a-docker-build-for-django-and-mysql
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "HOST": get_secret("DATABASE_HOST"),
        "PORT": "3306",
        "NAME": get_secret("DATABASE_NAME"),
        # <-----이부분 중요 !! db인스턴스명이 아니라 유저이름과 동일하게 SET!
        "USER": get_secret("DATABASE_USER"),
        "PASSWORD": get_secret("DATABASE_PASSWORD"),
    }
}
