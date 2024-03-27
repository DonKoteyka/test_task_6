from django.contrib import admin

from application.models import Posts, Comments, Likes

class CommentInline(admin.TabularInline):
    model = Comments

@admin.register(Posts)
class Posts(admin.ModelAdmin):
    list_display = ('pk', 'title', 'description', 'user', 'created_at')
    inlines = (CommentInline,)
    # search_fields = ('text',)
    # list_filter = ('pub_date',)
    # empty_value_display = '-пусто-'


# @admin.register(Comments)
# class CommentsAdmin(admin.ModelAdmin):
#     list_display = ('pk', 'user', 'post', 'comment', 'created_at')
    # search_fields = ('text',)
    # list_filter = ('created',)
    # empty_value_display = '-пусто-'


@admin.register(Likes)
class LikesAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'posts')
