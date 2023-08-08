-- sudo apt install postgresql postgresql-contrib
-- sudo -u postgres psql
-- create role dbadmin with login password 'password';

create database temperature_tracking;
grant all privileges on database temperature_tracking to dbadmin;

-- psql -U dbadmin -d temperature_tracking
CREATE TABLE temperatures (
    id SERIAL PRIMARY KEY,
    time_stamp TIMESTAMPTZ NOT NULL DEFAULT now(),
    temperature DECIMAL(6,3) NOT NULL
);

-- insert into temperatures (temperature) values (25.3);

create table room_temps (
    id SERIAL PRIMARY KEY,
    time_stamp timestamptz not null default now(),
    temperature decimal(6,3) not null
);

INSERT INTO temperatures (id, time_stamp, temperature)
VALUES (0, '2023-06-08 08:15', 35.8);