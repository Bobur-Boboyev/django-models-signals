from django.db.models import Q
from .models import Airport

def filter_queryset(queryset: Airport, search):
    if search:
            queryset = queryset.filter(
                Q(name__icontains=search)
                | Q(airport_code__icontains=search)
                | Q(icao_code__icontains=search)
                | Q(city__icontains=search)
                | Q(city_code__icontains=search)
                | Q(country__icontains=search)
                | Q(country_code__icontains=search)
                | Q(state__icontains=search)
                | Q(slug__icontains=search)
            )

    return queryset