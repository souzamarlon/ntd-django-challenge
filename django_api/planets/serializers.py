

from .models import Planet
from rest_framework import serializers

class PlanetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Planet
        fields = ['id', 'name', 'population', 'terrains', 'climates']