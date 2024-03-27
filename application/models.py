from django.db import models
from django.contrib.auth.models import User


class Posts(models.Model):
    """Объявление."""

    title = models.TextField()
    description = models.TextField(default='')
    user = models.ForeignKey(User, on_delete=models.CASCADE ,related_name='post')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
    def __str__(self):
        return self.title

class Comments(models.Model):
    """Комментарии """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment')
    post = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name='comment')
    created_at = models.DateTimeField(auto_now_add=True)
    comment = models.TextField(null=True, blank=True,)

    class Meta:
        verbose_name = 'Комментарии'
        verbose_name_plural = 'Комментарий'

    def __str__(self):
        return self.comment

class Likes(models.Model):
    """Лайки"""
    posts = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name='like')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='like', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    class Meta:
        verbose_name = 'Лайк'
        verbose_name_plural = 'Лайки'


    # def __str__(self):
    #     return f'{self.user.get_username()} likes {self.posts.text}'