from django.db import models
from nocapapi.models import RosterUser


class Roster(models.Model):
    user = models.ForeignKey(RosterUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=800, null=True)