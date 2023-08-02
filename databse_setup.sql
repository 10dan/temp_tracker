-- sudo apt install postgresql postgresql-contrib
-- sudo -u postgres psql
-- create role dbadmin with login password 'password';

create database temperature_tracking;
grant all privileges on database temperature_tracking to dbadmin;

-- psql -U dbadmin -d temperature_tracking
create table temperatures (
    time_stamp timestamptz not null default now(),
    temperature decimal(6,3) not null
);

insert into temperatures (temperature) values (25.3);