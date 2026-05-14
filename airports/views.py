from rest_framework import viewsets

from .models import Airport
from .serializers import AirportSerializer
from .utils import filter_queryset


class AirportViewSet(viewsets.ModelViewSet):
    queryset = Airport.objects.filter(is_active=True)
    serializer_class = AirportSerializer

    def get_queryset(self):
        queryset = super().get_queryset()

        search = self.request.query_params.get("search")

        if search:
            queryset = filter_queryset(queryset, search)

        return queryset