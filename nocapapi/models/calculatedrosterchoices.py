from django.db import models

class CalculatedRosterChoices(models.Model):

    character = models.ForeignKey("Character", on_delete=models.CASCADE)
    calculated_roster = models.ForeignKey("CalculatedRoster", on_delete=models.CASCADE, related_name="calculatedrosterchoices")
    damage = models.BigIntegerField()
    healing = models.BigIntegerField()
    kills = models.IntegerField()
    deaths = models.IntegerField()
    assists = models.IntegerField()
    group = models.IntegerField(null=True)

    # @property
    # def total_damage(self):
    #     return self.__total_damage
    # @total_damage.setter
    # def total_damage(self, value):
    #     self.__total_damage = value
    # @property
    # def total_healing(self):
    #     return self.__total_healing
    # @total_healing.setter
    # def total_healing(self, value):
    #     self.__total_healing = value
    # @property
    # def total_kills(self):
    #     return self.__total_kills
    # @total_kills.setter
    # def total_kills(self, value):
    #     self.__total_kills = value
    # @property
    # def total_deaths(self):
    #     return self.__total_deaths

    # @total_deaths.setter
    # def total_deaths(self, value):
    #     self.__total_deaths = value   
        
        
       