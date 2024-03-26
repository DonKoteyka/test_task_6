from django.conf import settings
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Posts(models.Model):
    """Объявление."""

    title = models.TextField()
    description = models.TextField(default='')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
    def __str__(self):
        return self.title

class Comments(models.Model):
    """Комментарии """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    post = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name='advertisement')
    created_at = models.DateTimeField(auto_now_add=True)
    comment = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'Комментарии'
        verbose_name_plural = 'Комментарий'

    def __str__(self):
        return self.comment

class Likes(models.Model):
    """Лайки"""
    posts = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='liked', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    class Meta:
        verbose_name = 'Лайк'
        verbose_name_plural = 'Лайки'


    def __str__(self):
        return f'{self.user.get_username()} likes {self.posts.text}'