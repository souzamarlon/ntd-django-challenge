from rest_framework.routers import DefaultRouter
from .views import PlanetViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'planet', PlanetViewSet)

urlpatterns = [
    path('', include(router.urls)),
]