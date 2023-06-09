from django.db import models


class PokedexCreature(models.Model):
    number = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    type1 = models.CharField(max_length=50)
    type2 = models.CharField(max_length=50, blank=True, null=True)
    total = models.IntegerField(blank=True, null=True)
    hp = models.IntegerField(blank=True, null=True)
    attack = models.IntegerField(blank=True, null=True)
    defense = models.IntegerField(blank=True, null=True)
    sp_attack = models.IntegerField(blank=True, null=True)
    sp_defense = models.IntegerField(blank=True, null=True)
    speed = models.IntegerField(blank=True, null=True)
    generation = models.IntegerField(blank=True, null=True)
    legendary = models.BooleanField(blank=True, null=True)


class Pokemon(models.Model):
    pokedex_creature = models.ForeignKey(PokedexCreature, on_delete=models.CASCADE)
    trainer_id = models.IntegerField(blank=True, null=True)
    nickname = models.CharField(max_length=100, blank=True, null=True)
    level = models.IntegerField(default=1)
    experience = models.IntegerField(default=1)

    def save(self, *args, **kwargs):
        # Assure level update invokes on give-xp and on update events
        if self.pk is not None:
            old_pokemon = Pokemon.objects.get(pk=self.pk)
            if self.experience != old_pokemon.experience:
                level_up = self.experience // 100 + 1
                if level_up > self.level:
                    self.level = level_up
        super().save(*args, **kwargs)
