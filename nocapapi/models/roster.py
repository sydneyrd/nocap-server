from django.db import models


class Roster(models.Model):
    user = models.ForeignKey("RosterUser", on_delete=models.CASCADE)
    name = models.CharField(max_length=800, null=True)