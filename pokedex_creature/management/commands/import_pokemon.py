import os
import csv
from django.core.management import BaseCommand
from pokedex_creature.models import PokedexCreature

class Command(BaseCommand):
    help = 'Import Pokémon data from CSV'

    def handle(self, *args, **options):
        with open('pokedex_creature/csv/pokemon.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                number = row['#']
                defaults = {
                    'name': row['Name'],
                    'type1': row['Type 1'],
                    'type2': row['Type 2'],
                    'total': row['Total'],
                    'hp': row['HP'],
                    'attack': row['Attack'],
                    'defense': row['Defense'],
                    'sp_attack': row['Sp. Atk'],
                    'sp_defense': row['Sp. Def'],
                    'speed': row['Speed'],
                    'generation': row['Generation'],
                    'legendary': row['Legendary'] == 'True'
                }
                pokedex_creature, _ = PokedexCreature.objects.get_or_create(number=number, defaults=defaults)
