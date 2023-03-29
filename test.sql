SELECT * FROM nocapapi_rosterchoices
WHERE id NOT IN (
    SELECT MIN(id) FROM 
    nocapapi_rosterchoices
    GROUP BY roster_id, character_id
);


SELECT * FROM nocapapi_rosterchoices
WHERE character_id IN (53, 62, 36, 99); 

DELETE FROM nocapapi_rosterchoices
WHERE id=261