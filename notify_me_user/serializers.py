from rest_framework import serializers
from notify_me_user.models import NotifyUser

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Busses
        fields = ['id', 'bus_route_number', 'created_at', 'updated_at', 'deleted_at']