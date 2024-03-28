"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from application.views import (CommentsViewSet, PostsViewSet,
                               UserCreateViewSet, UserLogInViewSet)

router = DefaultRouter()

router.register("news", PostsViewSet, basename="news")
router.register(r"news/(?P<news_id>\d+)/comments", CommentsViewSet, basename="comment")


urlpatterns = [
    path("api/", include(router.urls)),
    path("admin/", admin.site.urls),
    path("api/auth/user/", UserCreateViewSet.as_view()),
    path("api/auth/", UserLogInViewSet.as_view()),
]
