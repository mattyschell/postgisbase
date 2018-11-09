# POSTGISBASE

Delusions of PostGrandeur.

# Provision Database, Schemas, Users, Functions

Database creation executes as the postgres superuser with trust authentication 
(no password).  We will create the gis user with the input PGBSUPERPASSWORD. 

    $ export PGBHOST="localhost"
    $ export PGBSUPERPASSWORD="BeMyDataBae!" 
    $ psql -h $PGBHOST -p 5432 -U postgres -v v1=$PGBSUPERPASSWORD -f ./setup/createdatabase.sql
    $ export PGPASSWORD=$PGBSUPERPASSWORD
    $ ./functions/installfunctions.sh "$PGBHOST"

# Unit Tests

    See regress/README.md for the dirty details.  Run all existing tests cleanly like:

   $ python regress/run_all_tests.py "regress/all_tests"

# Integration Tests

    Maybe

# Teardown Testing Environment

    Probably

