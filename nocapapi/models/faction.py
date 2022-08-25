from django.db import models

class Faction(models.Model):
    name = models.CharField(max_length=100)