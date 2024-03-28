from django.contrib import admin

from application.models import Comments, Likes, Posts


class CommentInline(admin.TabularInline):
    model = Comments
    extra = 1


class LikestInline(admin.TabularInline):
    model = Likes
    extra = 1


@admin.register(Posts)
class Posts(admin.ModelAdmin):
    list_display = ("pk", "title", "description", "user", "created_at")
    inlines = (CommentInline, LikestInline)
