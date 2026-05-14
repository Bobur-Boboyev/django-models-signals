from django.contrib import admin
from .models import Airport


@admin.register(Airport)
class AirportAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "airport_code",
        "icao_code",
        "city",
        "country",
        "airport_type",
        "is_active",
        "is_24_hours",
        "supports_cargo",
    )
        
    list_filter = (
        "airport_type",
        "is_active",
        "is_24_hours",
        "supports_cargo",
        "supports_international_flights",
        "country",
        "city",
        "state",
    )
    
    search_fields = (
        "name",
        "airport_code",
        "icao_code",
        "city",
        "city_code",
        "country",
        "country_code",
        "state",
        "slug",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    fieldsets = (
        ("Core Information", {
            "fields": (
                "name",
                "airport_code",
                "icao_code",
                "slug",
                "airport_type",
            )
        }),

        ("Location", {
            "fields": (
                "city",
                "city_code",
                "state",
                "state_code",
                "country",
                "country_code",
                "address",
                "zip_code",
                "latitude",
                "longitude",
                "timezone",
            )
        }),

        ("Operations", {
            "fields": (
                "terminals",
                "runways",
                "elevation_ft",
                "website",
                "phone_number",
                "email",
            )
        }),

        ("Capabilities", {
            "fields": (
                "is_active",
                "is_24_hours",
                "supports_cargo",
                "supports_international_flights",
            )
        }),

        ("SEO / Description", {
            "fields": (
                "description",
            )
        }),

        ("Audit", {
            "fields": (
                "created_at",
                "updated_at",
            )
        }),
    )

    list_select_related = ()
    list_per_page = 25

    prepopulated_fields = {
        "slug": ("name", "airport_code")
    }

    list_display_links = ("name", "airport_code")
    ordering = ("country", "city", "name")

    actions = ["make_active", "make_inactive"]
    
    @admin.action(description="Activate selected airports")
    def make_active(self, request, queryset):
        queryset.update(is_active=True)

    @admin.action(description="Deactivate selected airports")
    def make_inactive(self, request, queryset):
        queryset.update(is_active=False)