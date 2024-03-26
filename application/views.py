from django.contrib.auth.password_validation import validate_password
from django.http import JsonResponse
from django_filters import DateFromToRangeFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password



from application.models import Posts
from application.permissions import IsOwnerOrAdmin
from application.serializers import PostSerializer, UserSerializer


class PostsViewSet(ModelViewSet):
    queryset = Posts.objects.all()
    serializer_class = PostSerializer
    http_method_names = ['get', 'post', 'put', 'delete']
    """ViewSet для объявлений."""
    permission_classes = (IsOwnerOrAdmin, IsAuthenticatedOrReadOnly)




# class UserCreateViewSet(CreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
#     def perform_create(self, serializer):
#         password = make_password(serializer.validated_data['password'])
#         serializer.validated_data['password'] = password
#         super().perform_create(serializer)
#         return Response({'status': 'OK'}, status=status.HTTP_200_OK)

# class UserLogInViewSet(CreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserLogInSerializer


class UserCreateViewSet(APIView):
    """ Класс для создания пользователя """
    def post(self, request, *args, **kwargs):
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
                    user.save()
                    return JsonResponse({'Status': True})
                else:
                    return JsonResponse({'Status': False, 'Errors': user_serializer.errors})

        return JsonResponse({'Status': False, 'Errors': 'Не указаны все необходимые аргументы'})

class AdminCreateViewSet(APIView):
    """ Класс для создания администратора """
    def post(self, request, *args, **kwargs):
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
                    user.is_superuser, user.is_staff = True
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






