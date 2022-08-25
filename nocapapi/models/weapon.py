from django.db import models

class Weapon(models.Model):
    name = models.CharField(max_length=100)