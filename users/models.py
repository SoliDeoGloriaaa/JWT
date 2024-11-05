from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Post(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name='Название',
        null=True
    )

    text = models.TextField(
        verbose_name='Текст',
        help_text='Введите текст поста',
    )

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='Автор',
    )

    def __str__(self):
        return f"{self.title}"
