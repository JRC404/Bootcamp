# SQL

* What do we already know about SQL?
    * A database
    * Structured query language - huh?
    * Language used to create tables
    * Retrieving data (Shelina says there is a lot of it)
    * Restoring data - backups etc

# Methods

## CRUD
* Create
* Read
* Update
* Delete    

* Who can do all of those things?
    * Depends

## The methods in SQL

* CREATE
    * Creates databases, Tables and Backups
```sql
CREATE DATABASE Bootcamp; -- comment this line out when done, so it doesn't say Database already exists
USE Bootcamp; -- this will tell the IDE to focus on the Bootcamp Database

CREATE TABLE Engineers (
	EngineerID int PRIMARY KEY, -- Primary Key ensures only one entry can have the unique ID
    EngineerName varchar(255), -- varchar limit is 255 characters
    Legs bit, -- bit == boolean
    EngineerLocation varchar(255) -- Location is an old default keyword, try not to use it
)
```
* INSERT
    * Data into our database / tables
```sql
INSERT INTO Engineers
VALUES(1, 'Sally Sallington', 0, 'Manchester'); -- Insert a record into the DB


INSERT INTO Engineers
VALUES(1, 'Sally Sallington', 0, 'Manchester'),
(1, 'Sally Sallington', 0, 'Manchester'); -- this won't work due to PK error
-- Duplicate entry: 1062 - Primary key already exists for number 1

INSERT INTO Engineers
VALUES(3, 'Bob Bobbington', 1, 'Leeds'),
(4, 'Tim Timmington', 1, 'Burnley');

INSERT INTO Engineers
VALUES(5, 'George Kontos', 0, 'Wyboston');

INSERT INTO Engineers
VALUES(6, 'George Kontos', 0, 'Wyboston'),
VALUES(7, 'George Kontos', 0, 'Wyboston'),
VALUES(8, 'George Kontos', 0, 'Wyboston'),
VALUES(9, 'George Kontos', 0, 'Wyboston');

SELECT * FROM Engineers; -- * is a wildcard... it means select ALL
```
* SELECT
    * Read data from a database / table

 ## Danger Zone in SQL

* UPDATE
    * Updates data in a database / table
* DELETE
    * Deletes data / databases / tables
* DROP
    * Drops data / tables / databases

# Backups

## Full Backup

* The entirety of your database is backed up daily, no matter what

## Differential Backup

* From the last full backup, you simply backup the additions that have been made
* You do a full backup on a Sunday... you backup the additions daily

## Incremental Backup

* Most recent changes from the last incremental backup