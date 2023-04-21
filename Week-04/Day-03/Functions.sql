SELECT AVG(EngineerSalary)
FROM Engineers;
-- '68441.1765'

SELECT AVG(EngineerSalary)
FROM Engineers
WHERE EngineerLocation = 'Manchester';

SELECT COUNT(EngineerSalary)
FROM Engineers;

SELECT COUNT(EngineerSalary)
FROM Engineers
WHERE EngineerLocation = 'Manchester';
-- 10

SELECT SUM(EngineerSalary)
FROM Engineers;
-- '2,327,000'

SELECT MIN(EngineerSalary)
FROM Engineers;

SELECT MIN(EngineerSalary)
FROM Engineers
WHERE EngineerLocation = 'Manchester';

SELECT MAX(EngineerSalary)
FROM Engineers;

SELECT MAX(EngineerSalary)
FROM Engineers
WHERE EngineerLocation = 'Burnley';

SELECT MIN(EngineerSalary) AS MinimumSalary
FROM Engineers;

SELECT EngineerName, MIN(EngineerSalary)
FROM Engineers;

SELECT EngineerName, MAX(EngineerSalary)
FROM Engineers;

SELECT * FROM Engineers;