#!/usr/bin/python3
# Displays all cities of a given state from the
# states table of the database hbtn_0e_4_usa.
# Safe from SQL injections.

import sys
import MySQLdb

if __name__ == "__main__":
  db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
  crs = db.cursor()
  crs.execute("SELECT * FROM `cities` as `c` \
                JOIN `states` as `s` \
                   ON `c`.`state_id` = `s`.`id` \
                ORDER BY `c`.`id`")
  for citie in crs.fetchall():
    if citie[4] == sys.argv[4]:
      print(" ,".join(citie[2]))
