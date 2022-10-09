from django.db import models

class CharLink(models.Model):
    character = models.ForeignKey("Character", on_delete=models.CASCADE, related_name="character")
    roster = models.ForeignKey("CalculatedRoster", on_delete=models.CASCADE, null=True, blank=True, related_name="calculated_roster")
    link = models.URLField("link", max_length=500)