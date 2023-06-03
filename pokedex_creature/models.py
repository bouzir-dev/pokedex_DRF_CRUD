from django.db import models


class PokedexCreature(models.Model):
    number = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    type1 = models.CharField(max_length=50)
    type2 = models.CharField(max_length=50, blank=True, null=True)
    total = models.IntegerField()
    hp = models.IntegerField()
    attack = models.IntegerField()
    defense = models.IntegerField()
    sp_attack = models.IntegerField()
    sp_defense = models.IntegerField()
    speed = models.IntegerField()
    generation = models.IntegerField()
    legendary = models.BooleanField()


class Pokemon(models.Model):
    pokedex_creature = models.ForeignKey(PokedexCreature, on_delete=models.CASCADE)
    trainer_id = models.IntegerField(blank=True, null=True)
    nickname = models.CharField(max_length=100, blank=True, null=True)
    level = models.IntegerField(default=1)
    experience = models.IntegerField(default=1)
