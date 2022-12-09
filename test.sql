SELECT SUM(damage) AS army_damage, SUM(healing) AS army_healing, 
SUM(kills) AS army_kills, 
SUM(deaths) AS army_deaths 
FROM nocapapi_calculatedrosterchoices

Where nocapapi_calculatedrosterchoices.calculated_roster_id = 4 
;


