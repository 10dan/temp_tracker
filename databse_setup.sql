-- sudo apt install postgresql postgresql-contrib
-- sudo -u postgres psql
-- create role dbadmin with login password 'password';

create database temperature_tracking;
grant all privileges on database temperature_tracking to dbadmin;

-- psql -U dbadmin -d temperature_tracking
CREATE TABLE temperatures (
    time_stamp TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    temperature DECIMAL(6,3) NOT NULL
);

insert into temperatures (temperature) values (25.3);