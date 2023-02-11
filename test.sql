SELECT SUM(damage) AS army_damage, SUM(healing) AS army_healing, 
SUM(kills) AS army_kills, 
SUM(deaths) AS army_deaths 
FROM nocapapi_calculatedrosterchoices

Where nocapapi_calculatedrosterchoices.calculated_roster_id = 33
;


SELECT SUM(nocapapi_calculatedrosterchoices.damage) AS army_damage,
       SUM(nocapapi_calculatedrosterchoices.healing) AS army_healing,
       SUM(nocapapi_calculatedrosterchoices.kills) AS army_kills,
       SUM(nocapapi_calculatedrosterchoices.deaths) AS army_deaths
FROM nocapapi_calculatedroster
JOIN nocapapi_calculatedrosterchoices
  ON nocapapi_calculatedroster.id = nocapapi_calculatedrosterchoices.calculated_roster_id
WHERE nocapapi_calculatedroster.id = 33;