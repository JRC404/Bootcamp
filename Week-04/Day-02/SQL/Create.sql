-- CREATE DATABASE Bootcamp;
-- semi colons are the end of a statement in sql
-- USE Bootcamp; -- Can't create database 'Bootcamp' database exists

CREATE TABLE Engineers (
	EngineerID int PRIMARY KEY,
    EngineerName varchar(255),
    Legs bit,
    EngineerLocation varchar(255)
)