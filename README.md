# POSTGISBASE

Delusions of PostGrandeur.

# Provision Database, Schemas, Users, Functions

Database creation executes as the postgres superuser with trust authentication 
(no password).  We will create the gis user with the input PGBSUPERPASSWORD. 

    $ export PGBHOST="localhost"
    $ export PGBSUPERPASSWORD="BeMyDataBae!" 
    $ psql -h $PGBHOST -p 5432 -U postgres -v v1=$PGBSUPERPASSWORD -f ./setup/createdatabase.sql
    $ ./functions/installfunctions.sh "$PGBHOST" "$PGBSUPERPASSWORD"

# Unit Tests

    See regress/README.md for the dirty details.  Run all tests cleanly like:

    $ <TBD dumb script of scripts here>

# Integration Tests

    Maybe?

