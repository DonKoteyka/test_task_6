from django.contrib.auth.password_validation import validate_password
from django.http import JsonResponse
from django_filters import DateFromToRangeFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import User


from application.models import Posts
from application.permissions import IsOwner
from application.serializers import AdvertisementSerializer, UserSerializer


class PostsViewSet(ModelViewSet):
    queryset = Posts.objects.all()
    serializer_class = AdvertisementSerializer
    """ViewSet для объявлений."""
    permission_classes = (IsOwner, IsAuthenticatedOrReadOnly)

    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['creator', 'status']
    # filterset_class = AdvertisementFilter

    # def perform_create(self, serializer):
    #     if Posts.objects.filter(status='OPEN', creator_id=self.request.user.id).count() >=10:
    #         raise ValueError('Превышение количества открытых объявлений')
    #     super().perform_create(serializer)
    # def perform_update(self, serializer):
    #     if Posts.objects.filter(status='OPEN', creator_id=self.request.user.id).exclude().count() >=10:
    #         raise ValueError('Превышение количества открытых объявлений')
    #     super().perform_update(serializer)

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer



# class UserViewSet(APIView):
#     def post(self, request, *args, **kwargs):
#         """
#             Process a POST request and create a new user.
#
#             Args:
#                 request (Request): The Django request object.
#
#             Returns:
#                 JsonResponse: The response indicating the status of the operation and any errors.
#             """
#         # проверяем обязательные аргументы
#         if {'username', 'first_name', 'last_name', 'email', 'password',}.issubset(request.data):
#
#             try:
#                 validate_password(request.data['password'])
#             except Exception as password_error:
#                 error_array = []
#                 # noinspection PyTypeChecker
#                 for item in password_error:
#                     error_array.append(item)
#                 return JsonResponse({'Status': False, 'Errors': {'password': error_array}})
#             else:
#                 # проверяем данные для уникальности имени пользователя
#
#                 user_serializer = UserSerializer(data=request.data)
#                 if user_serializer.is_valid():
#                     # сохраняем пользователя
#                     admin = user_serializer.save()
#                     admin.set_password(request.data['password'])
#                     admin.save()
#
#                     return JsonResponse({'Status': True})
#                 else:
#                     return JsonResponse({'Status': False, 'Errors': user_serializer.errors})
#
#         return JsonResponse({'Status': False, 'Errors': 'Не указаны все необходимые аргументы'})






