import sys
import os
import subprocess
import itertools

# this one must be set using the real password
#     $ export PGPASSWORD="BeMyDataBae!"
# database and user can be externalized through
#     PGBDATABASE, and PGBUSER environmentals 
#     Defaults to dmi and gis respectively if not set
# this one is optional
#     $ export PGBHOST="localhost" 
# python regress/run_test.py "regress/dummy.sql" "regress/dummy_expected"


class dbi(object):

    def __init__(self
                ,databasehost
                ,database
                ,databaseuser):

        self.dbhost = databasehost
        self.db = database
        self.dbuser = databaseuser
        
    def sql(self
           ,sqlfile):
                    
        psqlcmd = "psql -tXA "
        psqlcmd += "-h {0} -U {1} -d {2} -f {3}".format(self.dbhost
                                                       ,self.dbuser
                                                       ,self.db
                                                       ,sqlfile)

        p1 = subprocess.Popen(psqlcmd
                             ,stdout=subprocess.PIPE
                             ,shell=True)

        output = p1.communicate()[0]

        return output.strip()        


class dossier(object):

    def __init__(self
                ,content):

        # content should be a list of text, one line each
        if type(content) is list:
            self.content = content
        else:
            raise ValueError('Input is not a list')

    @classmethod
    def fromText(cls
                ,text):

        # supports all line ending types
        return cls(text.splitlines())

    @classmethod
    def fromFile(cls
                ,fname):

        # open with no newline set translates all line endings to \n
        with open(fname) as f:
            incontent = f.readlines()

        return cls([x.strip() for x in incontent])

    def getDirt(self
               ,content):
        
        # expected test results should be input to getDirt as clean content
        # tests (self) produce dirty dossiers
        
        dirt = []
        for testline, expectedline in itertools.izip_longest(self.content, 
                                                             content):
            if testline != expectedline:
                dirt.append('expected: {0}'.format(expectedline))
                dirt.append('test: {0}'.format(testline))
            else:
                # space reserved for debugging 
                pass                

        return dirt

def run_simple_test(testscript
                   ,testexpected):

    if not os.path.isfile(testexpected):
        msg = "I cannot find the expected file at {0}".format(testexpected)
        print msg
        raise ValueError(msg)

    # this is likely defaulted here, not set as an environmental 
    pgbhost = os.getenv('PGBHOST', 'localhost') 

    # expect these to be defaults also. Optional environmental overiddes
    pgbdatabase = os.getenv('PGBDATABASE', 'dmi')
    pgbuser = os.getenv('PGBUSER', 'gis')

    mydbi = dbi(pgbhost
               ,pgbdatabase
               ,pgbuser)
    
    sqloutput = mydbi.sql(testscript)

    testdossier = dossier.fromText(sqloutput)
    expecteddossier = dossier.fromFile(testexpected)
 
    dirtydossier = testdossier.getDirt(expecteddossier.content)

    if len(dirtydossier) > 0:
        print "failed test {0} comparing output to {1}".format(testscript
                                                              ,testexpected)
        for dirtyline in dirtydossier:
            print "{0}{1}".format('   '
                                 ,dirtyline) 
    else:
        print "{0}".format('.')


if __name__ == "__main__":

    if len(sys.argv) != 3:
        msg = "I {0} request but 2 inputs, the test sql and expected ".format(sys.argv[0])
        msg += "output file. Instead I have been given {0} inputs".format(len(sys.argv) - 1)                                                   
        print msg                                                                        
        raise ValueError(msg)

    ptestscript = sys.argv[1]   
    ptestexpected = sys.argv[2]

    run_simple_test(ptestscript
                   ,ptestexpected)