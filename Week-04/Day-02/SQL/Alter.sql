ALTER TABLE Engineers
ADD Salary int;

UPDATE Engineers
SET Salary = 50000
WHERE EngineerID > 0;

ALTER TABLE Engineers
RENAME COLUMN Salary TO EngineerSalary;

-- If the above code doesn't work for renaming columns, try the below...
ALTER TABLE Engineers
CHANGE Salary EngineerSalary int;

ALTER TABLE Engineers
DROP COLUMN Legs;

SELECT * FROM Engineers;