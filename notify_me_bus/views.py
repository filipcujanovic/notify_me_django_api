from notify_me_bus.serializers import BussesSerializer, BussesUsersSerializer, CurrentBussesRouteChangesSerializer
from notify_me_bus.models import Busses, BussesUsers, CurrentBussesRouteChanges
from rest_framework import viewsets
from rest_framework import pagination


class BussesViewSet(viewsets.ModelViewSet):
    queryset = Busses.objects.all()
    serializer_class = BussesSerializer

    def get_queryset(self):
        if (self.request.query_params.get('deleted')):
            return Busses.objects.all()

        return Busses.objects.filter(deleted_at=None)


class BussesUsersViewSet(viewsets.ModelViewSet):
    queryset = BussesUsers.objects.all()
    serializer_class = BussesUsersSerializer

    def get_queryset(self):
        if (self.request.query_params.get('deleted')):
            return BussesUsers.objects.all()

        return BussesUsers.objects.filter(deleted_at=None)


class CurrentBussesRouteChangesViewSet(viewsets.ModelViewSet):
    queryset = CurrentBussesRouteChanges.objects.all()
    serializer_class = CurrentBussesRouteChangesSerializer

    def get_queryset(self):
        if (self.request.query_params.get('deleted')):
            return CurrentBussesRouteChanges.objects.all()

        return CurrentBussesRouteChanges.objects.filter(deleted_at=None)