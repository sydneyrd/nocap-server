from django.db import models
from django.db.models import Sum, Aggregate


class CalculatedRoster(models.Model):
    user = models.ForeignKey("RosterUser", on_delete=models.CASCADE)
    rosterName = models.CharField(max_length=800, null=True)
    roster = models.ForeignKey("Roster", on_delete=models.SET_NULL, null=True, related_name="calculated")
    
    @property
    def total_damage(self):
        return self.calculatedrosterchoices.Aggregate(total_damage=Sum('damage'))['total_damage']

    @property
    def total_healing(self):
        return self.calculatedrosterchoices.aggregate(total_healing=Sum('healing'))['total_healing']

    @property
    def total_kills(self):
        return self.calculatedrosterchoices.aggregate(total_kills=Sum('kills'))['total_kills']

    @property
    def total_deaths(self):
        return self.calculatedrosterchoices.aggregate(total_deaths=Sum('deaths'))['total_deaths']