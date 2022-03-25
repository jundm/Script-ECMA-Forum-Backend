"""
Django settings for backend project.

Generated by 'django-admin startproject' using Django 4.0.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
import json
from django.core.exceptions import ImproperlyConfigured
from datetime import timedelta
from django.utils.translation import gettext_lazy as _

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent
secret_file = BASE_DIR / ".secrets.json"

with open(secret_file) as f:
    secrets = json.loads(f.read())


def get_secret(common, secrets=secrets):
    """비밀 변수를 가져오거나 명시적 예외를 반환한다."""
    try:
        return secrets[common]
    except KeyError:
        error_msg = "Set the {} environment variable".format(common)
        raise ImproperlyConfigured(error_msg)


SECRET_KEY = get_secret("SECRET_KEY")


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

DEBUG = True

ALLOWED_HOSTS = []


# Application definition


DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

# django-allauth https://django-allauth.readthedocs.io/en/latest/configuration.html
# dj-rest-auth https://dj-rest-auth.readthedocs.io/en/latest/installation.html
# rest_framework https://www.django-rest-framework.org
# rest_framework-simplejwt https://django-rest-framework-simplejwt.readthedocs.io/en/latest/
# django-cors-headers https://github.com/adamchainz/django-cors-headers
# djoser https://djoser.readthedocs.io/en/latest/getting_started.html


THIRD_PARTY_APPS = [
    "corsheaders",
    "djoser",
    "django_filters",
    "rest_framework",
    "rest_framework_simplejwt",
    "rest_framework_simplejwt.token_blacklist",
]
# account: 커스텀 유저 & 회원가입
PROJECT_APPS = [
    "accounts",
    "posts",
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + PROJECT_APPS

# https://docs.djangoproject.com/en/4.0/topics/i18n/translation/#how-django-discovers-language-preference
# translation: LocaleMiddleware가  session 뒤 common 앞이여야 한다
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "backend.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "backend.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# 프로젝트를 시작할때 사용자 정의 모델 사용(마이그레이션을 늦게 하는 이유)
# https://docs.djangoproject.com/en/4.0/topics/auth/customizing/#using-a-custom-user-model-when-starting-a-project
AUTH_USER_MODEL = "accounts.CustomUser"

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = "ko"

TIME_ZONE = "Asia/Seoul"

USE_I18N = True  # 장고 번역 시스템 활성화 여부
USE_L10N = True  # 현지화 데이터 형식 사용 여부
USE_TZ = True  # 시간대 인식 여부

LOCALE_PATHS = [
    BASE_DIR / "locale",
]

# 세팅방법 https://docs.djangoproject.com/en/4.0/ref/settings/#languages
# 언어코드 https://github.com/django/django/blob/main/django/conf/global_settings.py
# 사용함수 https://docs.djangoproject.com/en/4.0/ref/utils/#django.utils.translation.gettext_lazy
# 컴파일 python manage.py compilemessages or django-admin compilemessages --ignore=cache --ignore=outdated/*/locale
# 관련문서 https://docs.djangoproject.com/en/4.0/ref/django-admin/#compilemessages

LANGUAGES = (
    ("ko", _("Koran")),
    ("ja", _("Japanese")),
    ("en", _("English")),
    ("zh-hans", _("Simplified Chinese")),
    ("zh-hant", _("Traditional Chinese")),
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "static"

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"


# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# https://velog.io/@ayoung0073/DRF-signup-login-jwt
## DRF
REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.AllowAny",
        # "rest_framework.permissions.IsAuthenticated",
    ],
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ],
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 100,
    "DEFAULT_FILTER_BACKENDS": ["django_filters.rest_framework.DjangoFilterBackend"],
}
# JWT
SIMPLE_JWT = {
    "AUTH_HEADER_TYPES": ("JWT",),
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=35),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
    "ALGORITHM": "HS256",
    "SIGNING_KEY": SECRET_KEY,
    "LEEWAY": 0,  # 만료시간에 여유를 주는 값
}

# DJOSER CONFIG
# uid관한 솔루션 https://protocolostomy.com/2021/05/06/user-activation-with-django-and-djoser/ # 결론: uid = pk 로 쓰기로 했다
# 밑에 설정 많은데 전부 기본값이다 바꿀꺼 있으면 바꿀려고 기본값이지만 명시해놓음
DJOSER = {
    "LOGIN_FIELD": "email",
    "USER_CREATE_PASSWORD_RETYPE": True,
    # "USERNAME_CHANGED_EMAIL_CONFIRMATION": True,
    # "PASSWORD_CHANGED_EMAIL_CONFIRMATION": True,
    # "SEND_CONFIRMATION_EMAIL": True,
    "SET_PASSWORD_RETYPE": True,
    "PASSWORD_RESET_CONFIRM_URL": "password/reset/confirm/{id}/{token}",
    "USERNAME_RESET_CONFIRM_URL": "email/reset/confirm/{id}/{token}",
    "ACTIVATION_URL": "activate/{id}/{token}",
    # "SEND_ACTIVATION_EMAIL": True,
    "HIDE_USERS": True,
    "SERIALIZERS": {
        # SERIALIZERS
        "activation": "djoser.serializers.ActivationSerializer",
        "password_reset": "djoser.serializers.SendEmailResetSerializer",
        "password_reset_confirm": "djoser.serializers.PasswordResetConfirmSerializer",
        "password_reset_confirm_retype": "djoser.serializers.PasswordResetConfirmRetypeSerializer",
        "set_password": "djoser.serializers.SetPasswordSerializer",
        "set_password_retype": "djoser.serializers.SetPasswordRetypeSerializer",
        "set_username": "djoser.serializers.SetUsernameSerializer",
        "set_username_retype": "djoser.serializers.SetUsernameRetypeSerializer",
        "username_reset": "djoser.serializers.SendEmailResetSerializer",
        "username_reset_confirm": "djoser.serializers.UsernameResetConfirmSerializer",
        "username_reset_confirm_retype": "djoser.serializers.UsernameResetConfirmRetypeSerializer",
        "user_create": "CustomUser.serializers.UserCreateSerializer",
        "user_create_password_retype": "djoser.serializers.UserCreatePasswordRetypeSerializer",
        "user_delete": "djoser.serializers.UserDeleteSerializer",
        "user": "djoser.serializers.UserSerializer",
        "current_user": "djoser.serializers.UserSerializer",
        "token": "djoser.serializers.TokenSerializer",
        "token_create": "djoser.serializers.TokenCreateSerializer",
    },
    "EMAILS": {
        # EMAILS
        "activation": "djoser.email.ActivationEmail",
        "confirmation": "djoser.email.ConfirmationEmail",
        "password_reset": "djoser.email.PasswordResetEmail",
        "password_changed_confirmation": "djoser.email.PasswordChangedConfirmationEmail",
        "username_changed_confirmation": "djoser.email.UsernameChangedConfirmationEmail",
        "username_reset": "djoser.email.UsernameResetEmail",
    },
    "CONSTANCE": {
        # CONSTANCE
        "messages": "djoser.constants.Messages",
    },
    "PERMISSIONS": {
        "activation": ["rest_framework.permissions.AllowAny"],
        "password_reset": ["rest_framework.permissions.AllowAny"],
        "password_reset_confirm": ["rest_framework.permissions.AllowAny"],
        "set_password": ["djoser.permissions.CurrentUserOrAdmin"],
        "username_reset": ["rest_framework.permissions.AllowAny"],
        "username_reset_confirm": ["rest_framework.permissions.AllowAny"],
        "set_username": ["djoser.permissions.CurrentUserOrAdmin"],
        "user_create": ["rest_framework.permissions.AllowAny"],
        "user_delete": ["djoser.permissions.CurrentUserOrAdmin"],
        "user": ["djoser.permissions.CurrentUserOrAdmin"],
        "user_list": ["djoser.permissions.CurrentUserOrAdmin"],
        "token_create": ["rest_framework.permissions.AllowAny"],
        "token_destroy": ["rest_framework.permissions.IsAuthenticated"],
    },
}

CORS_ALLOWED_ORIGINS = [
    # "my_url",
]
