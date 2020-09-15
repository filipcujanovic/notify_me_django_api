
from django.contrib.auth.models import User
from notify_me_user.serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import viewsets
from notify_me_user.permissions import AllowPostAnyReadAuthenticatedUser

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowPostAnyReadAuthenticatedUser]

    def get_queryset(self):
        if (self.request.query_params.get('username')):
            return User.objects.filter(username=self.request.query_params.get('username'))

        return User.objects.all()

class MeViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowPostAnyReadAuthenticatedUser]

    def list(self, request, *args, **kwargs):
        instance = request.user
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
