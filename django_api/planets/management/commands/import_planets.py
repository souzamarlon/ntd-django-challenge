import requests
from django.core.management.base import BaseCommand
from planets.models import Planet


class Command(BaseCommand):
    help = 'Imports planets from SWAPI GraphQL and stores them in the database'

    def handle(self, *args, **kwargs):
        url = "https://swapi-graphql.netlify.app/.netlify/functions/index?query=query%20Query%20{allPlanets{planets{name%20population%20terrains%20climates}}}"

        response = requests.get(url)

        planets_data = response.json().get('data', {}).get('allPlanets', {}).get('planets', [])

        for item in planets_data:
            name = item.get("name")
            if not name:
                continue

            Planet.objects.get_or_create(
                name=name,
                defaults={
                    "population": item.get("population", None),
                    "terrains": item.get("terrains", []),
                    "climates": item.get("climates", [])
                }
            )

        self.stdout.write(self.style.SUCCESS(f"Imported planets."))
