from rest_framework import serializers
from .models import PokedexCreature, Pokemon


class PokedexCreatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = PokedexCreature
        fields = '__all__'


class PokemonSerializer(serializers.ModelSerializer):
    pokedex_creature_id = serializers.PrimaryKeyRelatedField(
        queryset=PokedexCreature.objects.all(),
        source='pokedex_creature',
        write_only=True
    )
    class Meta:
        model = Pokemon
        fields = ['pokedex_creature_id', 'trainer_id', 'nickname', 'level', 'experience']

    def create(self, validated_data):
        pokedex_creature = validated_data['pokedex_creature']
        nickname = validated_data.get('nickname') or pokedex_creature.name

        pokemon = Pokemon.objects.create(
            pokedex_creature=pokedex_creature,
            nickname=nickname,
            trainer_id=validated_data.get('trainer_id'),
            level=validated_data.get('level', 1),
            experience=validated_data.get('experience', 0)
        )

        return pokemon

class GiveXPSerializer(serializers.Serializer):
    amount = serializers.IntegerField(min_value=1)
