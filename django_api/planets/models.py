from django.db import models

# Create your models here.
class Planet(models.Model):
    name = models.CharField(max_length=100)
    population = models.BigIntegerField(null=True, blank=True)
    terrains = models.JSONField(null=True, blank=True) 
    climates = models.JSONField(null=True, blank=True)

    def __str__(self):
        return self.name