-- Creates a full table in the database

CREATE TABLE IF NOT EXISTS second_table(id INT, name VARCHAR(256), score INT)
INSERT INTO second_table (id, name, score) VALUES ([1, 2, 3, 4], ['John', 'Alex', 'Bob', 'George'], [10, 3, 14, 8]);
