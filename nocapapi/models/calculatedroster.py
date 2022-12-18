from django.db import models


class CalculatedRoster(models.Model):
    user = models.ForeignKey("RosterUser", on_delete=models.CASCADE)
    rosterName = models.CharField(max_length=800, null=True)
    roster = models.ForeignKey("Roster", on_delete=models.SET_NULL, null=True, related_name="calculated")
 
    
 
    @property
    def total_damage(self):
        return self.__results__

    @total_damage.setter
    def total_damage(self, value):
        self.__results__= value   
        
    @property
    def total_healing(self):
        return self.__total_healing
    @total_healing.setter
    def total_healing(self, value):
        self.__total_healing = value
    @property
    def total_kills(self):
        return self.__total_kills
    @total_kills.setter
    def total_kills(self, value):
        self.__total_kills = value
    @property
    def total_deaths(self):
        return self.__total_deaths

    @total_deaths.setter
    def total_deaths(self, value):
        self.__total_deaths = value   
        