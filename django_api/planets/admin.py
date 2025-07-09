from django.contrib import admin

# Register your models here.
from .models import Planet
@admin.register(Planet)


class PlanetAdmin(admin.ModelAdmin):
    list_display = ('name', 'population', 'terrains', 'climates')
    search_fields = ('name',)
    ordering = ('name',)