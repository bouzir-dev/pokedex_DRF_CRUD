from rest_framework import serializers
from .models import PokedexCreature, Pokemon


class PokedexCreatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = PokedexCreature
        fields = '__all__'


class PokemonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pokemon
        fields = '__all__'


class GiveXPSerializer(serializers.Serializer):
    amount = serializers.IntegerField(min_value=1)
