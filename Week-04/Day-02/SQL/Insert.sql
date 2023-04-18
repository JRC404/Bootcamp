-- INSERT INTO Engineers
-- VALUES(2, 'Sally Sallington', 0, 'Manchester');
-- Duplicate entry: 1062 - Primary key already exists for number 1

INSERT INTO Engineers
VALUES(3, 'Bob Bobbington', 1, 'Leeds'),
(4, 'Tim Timmington', 1, 'Burnley');


SELECT * FROM Engineers; -- * is a wildcard... it means select ALL