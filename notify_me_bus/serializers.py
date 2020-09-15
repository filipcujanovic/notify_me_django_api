from rest_framework import serializers
from notify_me_bus.models import Busses, BussesUsers, CurrentBussesRouteChanges

class BussesSerializer(serializers.HyperlinkedModelSerializer):
    created_at = serializers.ReadOnlyField()
    updated_at = serializers.ReadOnlyField()
    deleted_at = serializers.ReadOnlyField()
    id = serializers.ReadOnlyField()
    
    class Meta:
        model = Busses
        fields = ['id', 'bus_route_number', 'created_at', 'updated_at', 'deleted_at']
        ordering = ['id']


class BussesUsersSerializer(serializers.HyperlinkedModelSerializer):
    created_at = serializers.ReadOnlyField()
    updated_at = serializers.ReadOnlyField()
    deleted_at = serializers.ReadOnlyField()
    id = serializers.ReadOnlyField()

    class Meta:
        model = BussesUsers
        fields = ['id', 'bus_id', 'user_id', 'created_at', 'updated_at', 'deleted_at']
        ordering = ['id']
        
        
class CurrentBussesRouteChangesSerializer(serializers.HyperlinkedModelSerializer):
    created_at = serializers.ReadOnlyField()
    updated_at = serializers.ReadOnlyField()
    deleted_at = serializers.ReadOnlyField()
    id = serializers.ReadOnlyField()

    class Meta:
        model = CurrentBussesRouteChanges
        fields = ['id', 'bus_id', 'route_change', 'created_at', 'updated_at', 'deleted_at']
        ordering = ['id']