# POSTGISBASE

Delusions of PostGrandeur.

# Dependencies

1. PostgreSQL with PostGIS extension
   1a. Developed with PostgreSQL 10.6 for Windows x86-64 and PostGIS 2.5.0
   1b. Privileges to create a database, users, schemas
   1c. Terminal with psql on PATH
2. Python (2.7) on PATH
 

# Provision Database, Schemas, Users, Functions

We will create a new 'gis' user with the input PGBSUPERPASSWORD. If your 
existing superuser connects via non-standard hosts, passwords, or users, 
externalize them first.

    $ export PGPORT=5433
    $ export PGPASSWORD=ILuvMyDataBae247
    $ export PGHOST=aws.dollar.dollar.bill
    $ export PGUSER=postgres2

Then run this.  Replace the new user password below if you like.

    $ export PGBSUPERPASSWORD=BeMyDataBae 
    $ psql -v v1=$PGBSUPERPASSWORD -f ./setup/createdatabase.sql
    $ export PGPASSWORD=$PGBSUPERPASSWORD
    $ ./functions/installfunctions.sh

# Unit Tests

    See regress/README.md for the dirty details.  Run all existing tests cleanly like:

   $ python regress/run_all_tests.py "regress/all_tests"

# Integration Tests

    Maybe

# Teardown Testing Environment

    Probably

