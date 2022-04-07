from storages.backends.s3boto3 import S3Boto3Storage
from django.conf import settings

# https://velog.io/@hwang-eunji/aws-s3-미디어-서버-설정-django-설정
# https://testdriven.io/blog/storing-django-static-and-media-files-on-amazon-s3/
# https://www.youtube.com/watch?v=ahBG_iLbJPM


class MediaStorage(S3Boto3Storage):
    location = "media"
    file_overwrite = False
