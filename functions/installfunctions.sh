printf "installfunctions.sh is compiling all functions\n"
printf "on database %s as user %s\n" "dmi" "gis"
# assume that dependency order will never be properly managed
# except by manually faffing about the lines in this file
psql -U gis -d dmi -f functions/dummy.sql
psql -U gis -d dmi -f functions/escapechars.sql
psql -U gis -d dmi -f functions/escapecharstab.sql
printf "exiting from installfunctions.sh"