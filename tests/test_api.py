from django.test import TestCase
from rest_framework.test import APIClient
from pokedex_creature.models import PokedexCreature, Pokemon

class APITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        # Create some PokedexCreature instances for testing
        PokedexCreature.objects.create(number=1, name='Pikachu', type1='Electric', generation=1, legendary=False)
        PokedexCreature.objects.create(number=2, name='Charizard', type1='Fire', type2='Flying', generation=1, legendary=False)
        PokedexCreature.objects.create(number=3, name='Mewtwo', type1='Psychic', generation=1, legendary=True)
        # Create a Pokemon instance for testing the give_xp action
        self.pokemon = Pokemon.objects.create(pokedex_creature_id=1, level=1, experience=0)

    def test_pokedex_filters(self):
        response = self.client.get('/pokedex/', {'type1': 'Electric'})
        self.assertEqual(response.status_code, 200)
        # Assert that the response contains only the filtered PokedexCreature instances
        self.assertEqual(response.data.get('count'), 1)

        self.assertEqual(response.data.get('results')[0]['name'], 'Pikachu')

    def test_give_xp_action(self):
        response = self.client.post(f'/pokemon/{self.pokemon.pk}/give_xp/', {'amount': 50})
        self.assertEqual(response.status_code, 200)
        # Assert that the experience is updated and the level remains 1 (since it's below 100)
        self.assertEqual(response.data['message'], 'Gave 50 experience to the Pokemon.')
        updated_pokemon = Pokemon.objects.get(pk=self.pokemon.pk)
        self.assertEqual(updated_pokemon.experience, 50)
        self.assertEqual(updated_pokemon.level, 1)

        response = self.client.post(f'/pokemon/{self.pokemon.pk}/give_xp/', {'amount': 100})
        self.assertEqual(response.status_code, 200)
        # Assert that the experience is updated and the level is incremented to 2 (100/100)
        self.assertEqual(response.data['message'], 'Gave 100 experience to the Pokemon.')
        updated_pokemon = Pokemon.objects.get(pk=self.pokemon.pk)
        self.assertEqual(updated_pokemon.experience, 150)
        self.assertEqual(updated_pokemon.level, 2)

        # Additional tests for other scenarios

