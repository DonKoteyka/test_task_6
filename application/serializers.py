from django.contrib.auth.models import User
from rest_framework import serializers

from application.models import Posts, Comments


class UserSerializer(serializers.ModelSerializer):
    """Serializer для пользователя."""

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'password',)
        read_only_fields = ('id',)



class PostSerializer(serializers.ModelSerializer):
    """Serializer для объявления"""

    user = serializers.SlugRelatedField(slug_field='username', read_only=True)
    comment = serializers.SerializerMethodField()
    like = serializers.SerializerMethodField()

    class Meta:
        model = Posts
        fields = ('id', 'user', 'title', 'description', 'created_at', 'comment', 'like' )


    def get_comment(self, obj):
        comments = obj.comment.all()
        comment_data = CommentsSerializer(comments, many=True).data
        return comment_data
    #
    def get_like(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            return obj.like.filter(user=request.user).exists()
        return False
    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)
    #     request = self.context.get('request')
    #     if request and not request.user.is_authenticated:
    #         representation.pop('like')
    #     return representation


class CommentsSerializer(serializers.ModelSerializer):
    """Serializer для комментариев"""
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Comments
        fields = ('id', 'user', 'post', 'created_at', 'comment')





