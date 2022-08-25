from django.db import models
from django.contrib.auth.models import User

class Character(models.Model):
    role = models.ForeignKey("Role", on_delete=models.CASCADE)
    faction = models.ForeignKey("Faction", on_delete=models.CASCADE)
    primary_weapon = models.ForeignKey("Weapon", on_delete=models.CASCADE, related_name="primaryweapon")
    secondary_weapon = models.ForeignKey("Weapon", on_delete=models.CASCADE, related_name="secondaryweapon")
    server = models.ForeignKey("Server", on_delete=models.CASCADE)
    character_name = models.CharField(max_length=250)
    user = models.ForeignKey("RosterUser", on_delete=models.CASCADE)
