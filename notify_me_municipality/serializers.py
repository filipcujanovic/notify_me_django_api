from rest_framework import serializers
from notify_me_municipality.models import Municipalities, MunicipalitiesUsers

class MunicipalitiesSerializer(serializers.HyperlinkedModelSerializer):
    created_at = serializers.ReadOnlyField()
    updated_at = serializers.ReadOnlyField()
    deleted_at = serializers.ReadOnlyField()
    id = serializers.ReadOnlyField()
    
    class Meta:
        model = Municipalities
        fields = ['id', 'name', 'created_at', 'updated_at', 'deleted_at']
        ordering = ['id']
        

class MunicipalitiesUsersSerializer(serializers.HyperlinkedModelSerializer):
    created_at = serializers.ReadOnlyField()
    updated_at = serializers.ReadOnlyField()
    deleted_at = serializers.ReadOnlyField()
    id = serializers.ReadOnlyField()

    class Meta:
        model = MunicipalitiesUsers
        fields = ['id', 'municipality_id', 'user_id', 'created_at', 'updated_at', 'deleted_at']
        ordering = ['id']