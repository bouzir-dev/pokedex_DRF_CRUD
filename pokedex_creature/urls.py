from django.urls import path
from .viewsets import *
from rest_framework import routers

app_name = 'pokemon_creature'

router = routers.DefaultRouter()
router.register(r'pokedex', PokedexCreatureViewSet)
router.register(r'pokemon', PokemonViewSet)

urlpatterns = [
    *router.urls,
    path('pokemon/<int:pk>/give-xp/', PokemonViewSet.as_view({'post': 'give_xp'}), name='pokemon-give-xp'),

]
