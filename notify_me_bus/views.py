from notify_me_bus.serializers import BussesSerializer, BussesUsersSerializer, CurrentBussesRouteChangesSerializer
from notify_me_bus.models import Busses, BussesUsers, CurrentBussesRouteChanges
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import filters

class BussesViewSet(viewsets.ModelViewSet):
    queryset = Busses.objects.all()
    serializer_class = BussesSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['bus_route_number']
    ordering = ['bus_route_number']

    def get_queryset(self):
        if (self.request.query_params.get('deleted')):
            return Busses.objects.all()

        return Busses.objects.filter(deleted_at=None)


class BussesUsersViewSet(viewsets.ModelViewSet):
    queryset = BussesUsers.objects.all()
    serializer_class = BussesUsersSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return BussesUsers.objects.filter(user_id=self.request.user.id)
    
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


class CurrentBussesRouteChangesViewSet(viewsets.ModelViewSet):
    queryset = CurrentBussesRouteChanges.objects.all()
    serializer_class = CurrentBussesRouteChangesSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return CurrentBussesRouteChanges.objects.all()