from .common import *
import json
from django.core.exceptions import ImproperlyConfigured

with open(".secrets.json") as f:
    secrets = json.loads(f.read())


def get_secret(setting, secrets=secrets):
    try:
        return secrets[setting]
    except KeyError:
        error_msg = "Set the {0} environment variable".format(setting)
        raise ImproperlyConfigured(error_msg)


DEBUG = os.environ.get("DEBUG") in ["1", "t", "true", "T", "True"]
ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "").split(",")

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "level": "ERROR",
            "class": "logging.StreamHandler",
        },
    },
    "loggers": {
        "django": {"handlers": ["console"], "level": "ERROR"},
    },
}

# s3 https://kdharchive.tistory.com/830

# https://stackoverflow.com/questions/67568575/how-to-connect-s3-amazon-to-your-django-project
# https://integer-ji.tistory.com/13
# AWS
AWS_S3_ACCESS_KEY_ID = os.environ[
    "AWS_S3_ACCESS_KEY_ID"
]  # .csv 파일에 있는 내용을 입력 Access key ID
AWS_S3_SECRET_ACCESS_KEY = os.environ[
    "AWS_S3_SECRET_ACCESS_KEY"
]  # .csv 파일에 있는 내용을 입력 Secret access key

AWS_REGION = "ap-northeast-2"

###S3 Storages
AWS_STORAGE_BUCKET_NAME = os.environ["AWS_STORAGE_BUCKET_NAME"]  # 설정한 버킷 이름
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
        "HOST": os.environ["DATABASE_HOST"],
        "PORT": "3306",
        "NAME": os.environ.get("DATABASE_NAME", "dbmasteruser"),
        # <-----이부분 중요 !! db인스턴스명이 아니라 유저이름과 동일하게 SET!
        "USER": os.environ["DATABASE_USER"],
        "PASSWORD": os.environ["DATABASE_PASSWORD"],
    }
}
