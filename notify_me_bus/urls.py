from django.urls import path, include
from rest_framework.routers import DefaultRouter
from notify_me_bus import views


router = DefaultRouter()
router.register(r'busses', views.BussesViewSet)
router.register(r'busses_users', views.BussesUsersViewSet)
router.register(r'bus_changes', views.CurrentBussesRouteChangesViewSet)

urlpatterns = [
    path('', include(router.urls)),
]