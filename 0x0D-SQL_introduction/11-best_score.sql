-- List all records with the best scores in the table

SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
