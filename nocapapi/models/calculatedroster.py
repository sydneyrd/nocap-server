from django.db import models
from django.db.models import Sum, Aggregate
from nocapapi.models import RosterUser, Roster, Server


class CalculatedRoster(models.Model):
    user = models.ForeignKey(RosterUser, on_delete=models.CASCADE)
    rosterName = models.CharField(max_length=800, null=True)
    roster = models.ForeignKey(Roster, on_delete=models.SET_NULL, null=True, related_name="calculated")
    is_public = models.BooleanField(default=False, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    server = models.ForeignKey(Server, on_delete=models.DO_NOTHING, null=True, blank=True)
    
    @property
    def total_damage(self):
        return self.calculatedrosterchoices.aggregate(total_damage=Sum('damage'))['total_damage']

    @property
    def total_healing(self):
        return self.calculatedrosterchoices.aggregate(total_healing=Sum('healing'))['total_healing']

    @property
    def total_kills(self):
        return self.calculatedrosterchoices.aggregate(total_kills=Sum('kills'))['total_kills']

    @property
    def total_deaths(self):
        return self.calculatedrosterchoices.aggregate(total_deaths=Sum('deaths'))['total_deaths']