from django.db import models

class Role(models.Model):
    name = models.CharField(max_length=100)