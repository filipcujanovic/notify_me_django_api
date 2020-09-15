from notify_me_municipality.models import Municipalities, MunicipalitiesUsers
from notify_me_municipality.serializers import MunicipalitiesSerializer, MunicipalitiesUsersSerializer
from rest_framework import viewsets
from rest_framework import permissions
from notify_me_municipality.permissions import AllowOnlyUserMunicipalities

class MunicipalitiesViewSet(viewsets.ModelViewSet):
    queryset = Municipalities.objects.all()
    serializer_class = MunicipalitiesSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if (self.request.query_params.get('deleted')):
            return Municipalities.objects.all()

        return Municipalities.objects.filter(deleted_at=None)


class MunicipalitiesUsersViewSet(viewsets.ModelViewSet):
    queryset = MunicipalitiesUsers.objects.all()
    serializer_class = MunicipalitiesUsersSerializer
    permission_classes = [AllowOnlyUserMunicipalities]

    def get_queryset(self):
        return MunicipalitiesUsers.objects.filter(user_id=self.request.user.id)
    
    def create(self, request, *args, **kwargs):
        if type(request.data) is list:
            for item in request.data:
                item['user_id'] = request.user.id
        else:
            request.data['user_id'] = request.user.id

        return super().create(request, *args, **kwargs)

    def get_serializer(self, *args, **kwargs):
        if "data" in kwargs:
            data = kwargs["data"]
            
            if isinstance(data, list):
                kwargs["many"] = True

        return super().get_serializer(*args, **kwargs)
