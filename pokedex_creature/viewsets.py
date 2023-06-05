from rest_framework import viewsets, generics
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import PokedexCreature, Pokemon
from .serializers import PokedexCreatureSerializer, PokemonSerializer, GiveXPSerializer, PokedexCreaturePartialSerializer
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend


class PokedexCreatureViewSet(viewsets.ModelViewSet, PageNumberPagination):
    queryset = PokedexCreature.objects.all()
    serializer_class = PokedexCreatureSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['type1', 'type2', 'generation', 'legendary']

    def get_serializer_class(self):
        if self.action == 'list':
            return PokedexCreaturePartialSerializer
        return PokedexCreatureSerializer


class PokemonViewSet(viewsets.ModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer

    @action(detail=True, methods=['post'], serializer_class=GiveXPSerializer)
    def give_xp(self, request, pk=None):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        pokemon = self.get_object()
        amount = int(request.data.get('amount', 0))
        pokemon.experience += amount
        pokemon.save()

        return Response({'message': f'Gave {amount} experience to the Pokemon.'})
