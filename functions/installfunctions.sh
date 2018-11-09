pgbhost=$1
printf "installfunctions.sh is compiling all functions\n"
printf "on host %s, database %s, as user %s\n" "$pgbhost" "dmi" "gis"
# assume from jump that dependency order will never be properly managed
# except by manually faffing about the lines in this file
psql -h $pgbhost -U gis -d dmi -f functions/dummy.sql
printf "exiting from installfunctions.sh"