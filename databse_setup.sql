-- sudo apt install postgresql postgresql-contrib
-- sudo -u postgres psql
-- create role dbadmin with login password 'password';

create database temperature_tracking;
grant all privileges on database temperature_tracking to dbadmin;

-- psql -U dbadmin -d temperature_tracking
CREATE TABLE room_temps (
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