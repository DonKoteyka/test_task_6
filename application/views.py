from django.contrib.auth.password_validation import validate_password
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token


from application.models import Posts, Likes
from application.permissions import IsOwnerOrAdmin
from application.scripts import delete_object
from application.serializers import PostSerializer, UserSerializer, CommentsSerializer


class PostsViewSet(ModelViewSet):
    """ViewSet для объявлений."""
    queryset = Posts.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsOwnerOrAdmin, IsAuthenticatedOrReadOnly)
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=True, methods=['post', 'delete'], permission_classes=[IsAuthenticated],)
    def like(self, request, pk=None):
        post = self.get_object()
        fields = {'posts': post, 'user': request.user}
        if_already_exists = Likes.objects.filter(**fields).exists()
        if request.method == 'DELETE':
            return delete_object(model=Likes,fields=fields, exist=if_already_exists, errors_message= 'Уже лайкнуто')
        if if_already_exists:
            return Response({'errors': 'Уже лайкнуто'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            like = Likes(**fields)
            like.save()
            return Response({'detail': 'Лайкнуто'},status=status.HTTP_201_CREATED)

class CommentsViewSet(ModelViewSet):
    """ViewSet для комментариев."""
    permission_classes = (IsOwnerOrAdmin, IsAuthenticatedOrReadOnly)
    serializer_class = CommentsSerializer

    def get_post(self):
        return get_object_or_404(Posts, pk=self.kwargs.get('news_id'))
    def get_queryset(self):
        return self.get_post().comment.all()
    def perform_create(self, serializer):
        serializer.save(post=self.get_post(), user=self.request.user)

class UserCreateViewSet(APIView):
    """ Класс для создания пользователя """
    def post(self, request, *args, **kwargs):
        admin = request.data.get('admin', False)
        if {'first_name', 'last_name', 'email', 'password',}.issubset(request.data):
            try:
                validate_password(request.data['password'])
            except Exception as password_error:
                error_array = []
                for item in password_error:
                    error_array.append(item)
                return JsonResponse({'Status': False, 'Errors': {'password': error_array}})
            else:
                user_serializer = UserSerializer(data=request.data)
                if user_serializer.is_valid():
                    user = user_serializer.save()
                    user.username = request.data['email']
                    user.set_password(request.data['password'])
                    user.is_superuser, user.is_staff = admin, admin
                    user.save()
                    return JsonResponse({'Status': True})
                else:
                    return JsonResponse({'Status': False, 'Errors': user_serializer.errors})

        return JsonResponse({'Status': False, 'Errors': 'Не указаны все необходимые аргументы'})


class UserLogInViewSet(APIView):
    """ Класс для авторизации пользователей """
    def post(self, request, *args, **kwargs):
        if {'email', 'password'}.issubset(request.data):
            user = authenticate(request, username=request.data['email'], password=request.data['password'])
            if user is not None:
                token, _ = Token.objects.get_or_create(user=user)
                return JsonResponse({'Status': True, 'Token': token.key})

            return JsonResponse({'Status': False, 'Errors': 'Не удалось авторизовать'})

        return JsonResponse({'Status': False, 'Errors': 'Не указаны все необходимые аргументы'})







