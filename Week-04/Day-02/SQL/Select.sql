SELECT * FROM Engineers;

SELECT EngineerID FROM Engineers;
SELECT Legs FROM Engineers;

SELECT * FROM Engineers
WHERE EngineerLocation = 'Manchester';

UPDATE Engineers
SET EngineerLocation = 'Wyboston'
WHERE EngineerID = 5;

SELECT * FROM Engineers;