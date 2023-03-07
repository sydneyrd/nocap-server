from django.db import models
from nocapapi.models import CalculatedRoster, Character

class CalculatedRosterChoices(models.Model):

    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    calculated_roster = models.ForeignKey(CalculatedRoster, on_delete=models.CASCADE, related_name="calculatedrosterchoices")
    damage = models.BigIntegerField()
    healing = models.BigIntegerField()
    kills = models.IntegerField()
    deaths = models.IntegerField()
    assists = models.IntegerField()
    group = models.IntegerField(null=True)
