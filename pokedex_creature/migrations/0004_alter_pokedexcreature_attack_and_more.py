# Generated by Django 4.2.1 on 2023-06-05 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokedex_creature', '0003_rename_pokedex_creature_id_pokemon_pokedex_creature'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokedexcreature',
            name='attack',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pokedexcreature',
            name='defense',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pokedexcreature',
            name='generation',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pokedexcreature',
            name='hp',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pokedexcreature',
            name='legendary',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pokedexcreature',
            name='sp_attack',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pokedexcreature',
            name='sp_defense',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='pokedexcreature',
            name='speed',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
