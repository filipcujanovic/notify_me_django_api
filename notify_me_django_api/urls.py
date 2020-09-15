from django.urls import path, include
from rest_framework.routers import DefaultRouter
from notify_me_bus.urls import router as bus_router
from notify_me_municipality.urls import router as municipalities_router
from notify_me_user.urls import router as users_router

router = DefaultRouter()
router.registry.extend(bus_router.registry)
router.registry.extend(municipalities_router.registry)
router.registry.extend(users_router.registry)


urlpatterns = [
    path('', include('notify_me_auth.urls')),
    path('', include(router.urls)),
]
