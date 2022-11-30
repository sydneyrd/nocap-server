SELECT SUM(damage) AS army_damage, SUM(healing) AS army_healing, 
SUM(kills) AS army_kills, 
SUM(deaths) AS army_deaths 
FROM nocapapi_calculatedrosterchoices

Where nocapapi_calculatedrosterchoices.calculated_roster_id = 10 
;


SELECT SUM(damage) AS army_damage, damage AS player_damage, SUM(healing) AS army_healing, healing AS player_healing,
SUM(kills) AS army_kills, kills as player_kills,
SUM(deaths) AS army_deaths, deaths as player_deaths 
FROM nocapapi_calculatedrosterchoices

Where nocapapi_calculatedrosterchoices.calculated_roster_id = 10
GROUP BY id 
;