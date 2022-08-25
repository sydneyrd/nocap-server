from django.db import models


class CalculatedRoster(models.Model):
    user = models.ForeignKey("RosterUser", on_delete=models.CASCADE)
    rosterName = models.CharField(max_length=800, null=True)
    roster = models.ForeignKey("Roster", on_delete=models.SET_NULL, null=True, related_name="calculated")
