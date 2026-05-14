from django.core.management.base import BaseCommand
from django.utils.text import slugify
from airports.models import Airport
import random


class Command(BaseCommand):
    help = "Seed airports with full data"

    def handle(self, *args, **kwargs):
        Airport.objects.all().delete()

        countries = [
            ("Uzbekistan", "UZ"),
            ("USA", "US"),
            ("UK", "GB"),
            ("Germany", "DE"),
            ("UAE", "AE"),
        ]

        cities = [
            ("Tashkent", "TAS"),
            ("London", "LON"),
            ("Berlin", "BER"),
            ("Dubai", "DXB"),
            ("New York", "NYC"),
        ]

        airport_types = [
            "international",
            "domestic",
            "private",
            "military",
            "cargo",
        ]

        airports = []

        for i in range(100):
            city, city_code = random.choice(cities)
            country, country_code = random.choice(countries)
            airport_type = random.choice(airport_types)

            name = f"{city} {airport_type.capitalize()} Airport {i}"

            airport = Airport(
                airport_code=f"AIR{i:04}",
                icao_code=f"ICAO{i:04}",

                name=name,
                slug=slugify(f"{name}-{i}"),

                city=city,
                city_code=city_code,

                state="State " + city if random.random() > 0.5 else None,
                state_code=city_code if random.random() > 0.5 else None,

                country=country,
                country_code=country_code,

                address=f"{city} International Zone {i}" if random.random() > 0.2 else None,
                zip_code=str(10000 + i) if random.random() > 0.3 else None,

                latitude=41.0 + random.random(),
                longitude=69.0 + random.random(),

                timezone="Asia/Tashkent" if country == "Uzbekistan" else "UTC",

                airport_type=airport_type,

                terminals=random.randint(1, 5),
                runways=random.randint(1, 4),

                elevation_ft=random.randint(100, 3000),

                website=f"https://{city.lower().replace(' ', '')}.airport.com",
                phone_number=f"+99890{random.randint(1000000, 9999999)}",
                email=f"info@{city.lower().replace(' ', '')}.com",

                is_active=True,
                is_24_hours=random.choice([True, False]),
                supports_cargo=random.choice([True, False]),
                supports_international_flights=random.choice([True, False]),

                description=f"This is {name}, one of the major aviation hubs in {country}.",
            )

            airports.append(airport)

        Airport.objects.bulk_create(airports)

        self.stdout.write(
            self.style.SUCCESS("100 airports successfully seeded with full data")
        )