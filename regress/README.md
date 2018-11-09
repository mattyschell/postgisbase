# Regression Tests For postgisbase Repository

Modeled loosely on https://trac.osgeo.org/postgis/wiki/DevWikiPGRegress

Also described here https://github.com/postgis/postgis/tree/svn-trunk/regress

## For Some Functionality: Create a test and expected output

Tuples only, expanded output, unaligned, field separator is pipe. The function
dummy was previously compiled from functions/dummy.sql.   

    $ psql.exe -t -X -A -F\| -h localhost -U gis -d dmi -f regress/dummy.sql > regress/dummy_expected

Produces file dummy_expected with contents

    X|X

## Run A Test

Following our leaders again https://github.com/postgis/postgis/blob/svn-trunk/regress/run_test.pl

Run the <testname>.sql test in gisbase@dmi on localhost, compare against <testname>_expected

    $ python regress/run_test.py "regress/dummy.sql" "regress/dummy_expected"

## Run All Tests

    $ python regress/run_all_tests.py "regress/all_tests"



