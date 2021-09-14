CREATE SCHEMA phoenix;

--Create table Phoenix
DROP TABLE IF EXISTS phoenix.metric;
CREATE TABLE phoenix.metric(
    id INT GENERATED ALWAYS AS IDENTITY,
    created_time timestamp with time zone DEFAULT now(),
    volatage INT NOT NULL,
    current INT NOT NULL,
    PRIMARY KEY(id)
);