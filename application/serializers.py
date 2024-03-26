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
    """Serializer для объявления."""

    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )
    liked = serializers.SerializerMethodField()
    likes_quantity = serializers.SerializerMethodField()
    comment_quantity = serializers.SerializerMethodField()
    comments = serializers.SerializerMethodField()

    class Meta:
        model = Posts
        fields = (
            'id', 'author','title', 'description', 'created_at', 'liked',
            'likes_quantity', 'comment_quantity', 'comments'
        )

    def get_likes_quantity(self, obj):
        return obj.likes.count()

    def get_comment_quantity(self, obj):
        return obj.comments.count()

    def get_comments(self, obj):
        comments = obj.comments.order_by('-created')[:10]
        comment_data = CommentsSerializer(comments, many=True).data
        return comment_data

    def get_liked(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            return obj.likes.filter(user=request.user).exists()
        return False

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        request = self.context.get('request')
        if request and not request.user.is_authenticated:
            representation.pop('liked')
        return representation


class CommentsSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )

    class Meta:
        model = Comments
        fields = ('id', 'author', 'text', 'post')




