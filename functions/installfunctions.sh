printf "installfunctions.sh is compiling all functions\n"
pgbhost=$1
pgbpassword=$2
printf "target host %s, database %s, user %s\n" "$pgbhost" "dmi" "gis"
# assume from jump that dependency order will never be properly managed
# except by manually faffing about the lines in this file
PGPASSWORD=$pgbpassword psql -h $pgbhost -U gis -d dmi -f functions/dummy.sql
printf "exiting from installfunctions.sh"