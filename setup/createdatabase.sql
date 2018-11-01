-- export GISSUPERPASSWORD="BeMyDataBae!"
-- psql -h localhost -p 5432 -U postgres -v v1=$GISSUPERPASSWORD -f createdb.sql
DROP DATABASE IF EXISTS dmi;
DROP USER gis;
CREATE DATABASE dmi;
CREATE USER gis WITH password :'v1'; 
GRANT ALL PRIVILEGES ON DATABASE dmi TO gis; 
\connect dmi
CREATE EXTENSION IF NOT EXISTS postgis;
-- because I know the pattern, this mimics my standard Oracle namespacing
-- gis user is me
-- gisbase acts like a package
-- parceling out data across schemas is new, wild, and out of control. But also kinda the same
CREATE SCHEMA gisbase AUTHORIZATION gis;
GRANT ALL ON SCHEMA gisbase TO gis;
GRANT USAGE ON SCHEMA gisbase TO public; 
CREATE SCHEMA gistestdata AUTHORIZATION gis;
GRANT ALL ON SCHEMA gistestdata to gis;
GRANT USAGE ON SCHEMA gistestdata TO public; 
