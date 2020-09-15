from django.urls import path, include
from rest_framework.routers import DefaultRouter
from notify_me_user import views

router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'me', views.MeViewSet)