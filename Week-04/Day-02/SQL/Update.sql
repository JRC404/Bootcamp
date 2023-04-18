UPDATE Engineers
SET EngineerLocation = 'Wyboston'
WHERE EngineerID = 5;

UPDATE Engineers
SET EngineerSalary = 60000
WHERE EngineerLocation = 'Manchester';

SELECT * FROM Engineers;
