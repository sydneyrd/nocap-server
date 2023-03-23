from django.db import models
from nocapapi.models import Roster, Character

class RosterChoices(models.Model):

    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    roster = models.ForeignKey(Roster, on_delete=models.CASCADE, related_name="rosterchoices")
    group = models.IntegerField(null=True)
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['roster', 'character'], name='unique_roster_character_choices')
        ]