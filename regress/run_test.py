import sys
import os
import subprocess

# database and user can be externalized through
# PGBDATABASE, and PGBUSER environmenalts. 
# Defaults to dmi and gis respectively, if not set
# this one is mandatory
# $ export PGPASSWORD="BeMyDataBae!"
# this one is optional
# $ export PGBHOST="localhost" 
# python regress/run_test.py "regress/dummy.sql"
#                            "regress/dummy_expected"


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

        print "psqlcommand is " + psqlcmd
        print "cwd is " + os.getcwd()
        p1 = subprocess.Popen(psqlcmd
                             ,stdout=subprocess.PIPE
                             ,shell=True)

        output = p1.communicate()[0]
        print "output is " + output 

        return output.strip()        


#sub diff
#{
#	my ($expected_file, $obtained_file) = @_;
#	my $diffstr = '';
#
#	if ( $sysdiff ) {
#		$diffstr = `diff --strip-trailing-cr -u $expected_file $obtained_file 2>&1`;
#		return $diffstr;
#	}
#
#	open(OBT, $obtained_file) || return "Cannot open $obtained_file\n";
#	open(EXP, $expected_file) || return "Cannot open $expected_file\n";
#	my $lineno = 0;
#	while (!eof(OBT) or !eof(EXP)) {
#		# TODO: check for premature end of one or the other ?
#		my $obtline=<OBT>;
#		my $expline=<EXP>;
#		$obtline =~ s/\r?\n$//; # Strip line endings
#		$expline =~ s/\r?\n$//; # Strip line endings
#		$lineno++;
#		if ( $obtline ne $expline ) {
#			my $diffln .= "$lineno.OBT: $obtline\n";
#			$diffln .= "$lineno.EXP: $expline\n";
#			$diffstr .= $diffln;
#		}
#	}
#	close(OBT);
#	close(EXP);
#	return $diffstr;
#}

#class run_simple_test (test.sql, expected)


if __name__ == "__main__":

    if len(sys.argv) != 3:
        msg = "I {0} request but 2 inputs, the test sql and expected ".format(sys.argv[0])
        msg += "output file. Instead I have been given {0} inputs".format(len(sys.argv) - 1)
                                                           
        print msg                                                                        
        raise ValueError(msg)

    ptestscript = sys.argv[1]   
    ptestexpected = sys.argv[2]

    # this is likely defaulted here 
    pgbhost = os.getenv('PGBHOST', 'localhost') 

    # expect these to be defaults. Optional overiddes
    pgbdatabase = os.getenv('PGBDATABASE', 'dmi')
    pgbuser = os.getenv('PGBUSER', 'gis')

    testdbi = dbi(pgbhost
                 ,pgbdatabase
                 ,pgbuser)
    
    sqloutput = testdbi.sql(ptestscript)

    print "sqloutput is " + sqloutput