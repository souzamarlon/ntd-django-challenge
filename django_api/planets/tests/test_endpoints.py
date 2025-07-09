import pytest
from model_bakery import baker
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from planets.models import Planet
from planets.serializers import PlanetSerializer

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def planet():
    return baker.make(
        Planet,
        name="Earth",
        population=7000000000,
        terrains=["Mountains"],
        climates=["Temperate"]
    )

@pytest.mark.django_db
def test_list_planets(api_client, planet):
    url = reverse('planet-list')
    response = api_client.get(url)
    planets = Planet.objects.all()
    serializer = PlanetSerializer(planets, many=True)
    assert response.status_code == status.HTTP_200_OK
    assert response.data == serializer.data

@pytest.mark.django_db
def test_retrieve_planet(api_client, planet):
    url = reverse('planet-detail', args=[planet.id])
    response = api_client.get(url)
    serializer = PlanetSerializer(planet)
    assert response.status_code == status.HTTP_200_OK
    assert response.data == serializer.data

@pytest.mark.django_db
def test_create_planet(api_client):
    url = reverse('planet-list')
    data = {
        "name": "Mars",
        "climates": ["Arid"],
        "terrains": ["Desert"],
        "population": 0
    }
    response = api_client.post(url, data, format='json')
    assert response.status_code == status.HTTP_201_CREATED
    assert Planet.objects.filter(name="Mars").exists()

@pytest.mark.django_db
def test_update_planet(api_client, planet):
    url = reverse('planet-detail', args=[planet.id])
    data = {
        "name": "Earth",
        "climates": ["Temperate"],
        "terrains": ["Plains"],
        "population": 8000000000
    }
    response = api_client.put(url, data, format='json')
    planet.refresh_from_db()
    assert response.status_code == status.HTTP_200_OK
    assert planet.terrains == ["Plains"]
    assert planet.population == 8000000000

@pytest.mark.django_db
def test_partial_update_planet(api_client, planet):
    url = reverse('planet-detail', args=[planet.id])
    data = {
        "population": 9000000000
    }
    response = api_client.patch(url, data, format='json')
    planet.refresh_from_db()
    assert response.status_code == status.HTTP_200_OK
    assert planet.population == 9000000000

@pytest.mark.django_db
def test_delete_planet(api_client, planet):
    url = reverse('planet-detail', args=[planet.id])
    response = api_client.delete(url)
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert not Planet.objects.filter(id=planet.id).exists()