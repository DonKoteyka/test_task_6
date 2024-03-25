from django.conf import settings
from django.db import models
from django.contrib.auth.models import User



class Posts(models.Model):
    """Объявление."""

    title = models.TextField()
    description = models.TextField(default='')
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )

class Comments(models.Model):
    """Комментарии и Лайки"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    adv = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name='advertisement')
    created_at = models.DateTimeField(auto_now_add=True)
    comment = models.TextField(null=True, blank=True)
    like = models.BooleanField(blank=True, null=True)

    class Meta:
        verbose_name = 'Комментарии'
        verbose_name_plural = 'Комментарий'

    def __str__(self):
        return self.comment

