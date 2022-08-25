from django.db import models

class RosterChoices(models.Model):

    character = models.ForeignKey("Character", on_delete=models.CASCADE)
    roster = models.ForeignKey("Roster", on_delete=models.CASCADE, related_name="rosterchoices")