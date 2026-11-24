DROP TABLE IF EXISTS recipes;
DROP SEQUENCE IF EXISTS recipes_id_seq;

CREATE SEQUENCE IF NOT EXISTS recipes_id_seq;
CREATE TABLE recipes (
    id SERIAL PRIMARY KEY,
    name text,
    cooking_time int,
    rating int CHECK (rating BETWEEN 1 AND 5)
);

INSERT INTO recipes (name, cooking_time, rating) VALUES ('Spaghetti Bolognese', 45, 5);
INSERT INTO recipes (name, cooking_time, rating) VALUES ('Chicken Curry', 60, 4);
INSERT INTO recipes (name, cooking_time, rating) VALUES ('Pancakes', 20, 3);
INSERT INTO recipes (name, cooking_time, rating) VALUES ('Caesar Salad', 15, 4);