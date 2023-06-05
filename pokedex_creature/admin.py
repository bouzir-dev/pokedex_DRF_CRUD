from django.contrib import admin
from .models import PokedexCreature, Pokemon

@admin.register(PokedexCreature)
class PokedexCreatureAdmin(admin.ModelAdmin):
    list_display = ('name', 'type1', 'type2', 'generation', 'legendary')
    list_filter = ('type1', 'type2', 'generation', 'legendary')
    search_fields = ('name', 'type1', 'type2')

@admin.register(Pokemon)
class PokemonAdmin(admin.ModelAdmin):
    list_display = ('nickname', 'pokedex_creature', 'trainer_id', 'level', 'experience')
    list_filter = ('pokedex_creature__type1', 'pokedex_creature__type2', 'pokedex_creature__generation', 'pokedex_creature__legendary')
    search_fields = ('nickname', 'pokedex_creature__name')

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.select_related('pokedex_creature')
        return queryset