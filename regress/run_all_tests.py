import sys
import os
import run_test

# this one must be set using the real password
#     $ export PGPASSWORD="BeMyDataBae!"
# database and user can be externalized through
#     PGBDATABASE, and PGBUSER environmentals 
#     Defaults to dmi and gis respectively if not set
# this one is optional
#     $ export PGBHOST="localhost" 
# $ python regress/run_all_tests.py "regress/all_tests"

if __name__ == "__main__":

    if len(sys.argv) != 2:
        msg = "I {0} request but 1 input, a list of tests ".format(sys.argv[0])
        msg += "Instead I have been given {0} inputs".format(len(sys.argv) - 1)                                                   
        print msg                                                                        
        raise ValueError(msg)

    if not os.path.isfile(sys.argv[1]):
        msg = "I {0} cannot find the expected file at {1}".format(sys.argv[0]
                                                                 ,sys.argv[1])
        print msg
        raise ValueError(msg)

    ptestlist = sys.argv[1]   

    with open(ptestlist) as f:
            tests = [line.rstrip() for line in f]

    for test in tests:
        run_test.run_simple_test('regress/{0}.sql'.format(test)
                                ,'regress/{0}_expected'.format(test))