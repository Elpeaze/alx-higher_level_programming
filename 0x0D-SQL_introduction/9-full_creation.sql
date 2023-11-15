-- Creates a full table in the database

CREATE TABLE IF NOT EXISTS second_table(id INT, name VARCHAR(256), score INT)
WHERE id = 1, 2, 3, 4 AND name = 'John', 'Alex', 'Bob', 'George' AND score = 10, 3, 14, 8;
