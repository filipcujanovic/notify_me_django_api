from django.urls import path, include
from rest_framework.routers import DefaultRouter
from notify_me_municipality import views


router = DefaultRouter()
router.register(r'municipalities', views.MunicipalitiesViewSet)
router.register(r'municipalities_users', views.MunicipalitiesUsersViewSet)
