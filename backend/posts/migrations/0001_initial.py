# Generated by Django 4.0.1 on 2022-03-20 11:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Comment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("content", models.TextField(verbose_name="내용")),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="작성일"),
                ),
                ("updated_at", models.DateTimeField(auto_now=True, verbose_name="수정일")),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="CommentAuthor_set",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="댓글작성자",
                    ),
                ),
                (
                    "like_user_set",
                    models.ManyToManyField(
                        blank=True,
                        related_name="like_comment_set",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ["-id"],
            },
        ),
        migrations.CreateModel(
            name="Post",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100, verbose_name="제목")),
                ("content", models.TextField(verbose_name="내용")),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="작성일"),
                ),
                ("updated_at", models.DateTimeField(auto_now=True, verbose_name="수정일")),
                (
                    "category",
                    models.CharField(
                        choices=[
                            ("free", "free"),
                            ("question", "question"),
                            ("hot", "hot"),
                            ("news", "news"),
                        ],
                        max_length=12,
                    ),
                ),
                ("hit", models.IntegerField(default=0)),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="PostAuthor_set",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="작성자",
                    ),
                ),
                (
                    "like_user_set",
                    models.ManyToManyField(
                        blank=True,
                        related_name="like_post_set",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ["-id"],
            },
        ),
        migrations.CreateModel(
            name="Tag",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="PostComment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100, verbose_name="제목")),
                ("content", models.TextField(verbose_name="내용")),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="작성일"),
                ),
                ("updated_at", models.DateTimeField(auto_now=True, verbose_name="수정일")),
                (
                    "answer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="PostAnswer_set",
                        to="posts.post",
                        verbose_name="원글",
                    ),
                ),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="PostCommentAuthor_set",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="답변작성자",
                    ),
                ),
                (
                    "like_user_set",
                    models.ManyToManyField(
                        blank=True,
                        related_name="like_post_comment_set",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ["-id"],
            },
        ),
        migrations.AddField(
            model_name="post",
            name="tag_set",
            field=models.ManyToManyField(blank=True, to="posts.Tag", verbose_name="태그"),
        ),
        migrations.CreateModel(
            name="CommentReply",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("content", models.TextField(verbose_name="내용")),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="작성일"),
                ),
                ("updated_at", models.DateTimeField(auto_now=True, verbose_name="수정일")),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="CommentReplyAuthor_set",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="대댓글작성자",
                    ),
                ),
                (
                    "comment",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="posts.comment"
                    ),
                ),
                (
                    "like_user_set",
                    models.ManyToManyField(
                        blank=True,
                        related_name="like_comment_reply_set",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ["-id"],
            },
        ),
        migrations.AddField(
            model_name="comment",
            name="post",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="posts.post"
            ),
        ),
    ]
