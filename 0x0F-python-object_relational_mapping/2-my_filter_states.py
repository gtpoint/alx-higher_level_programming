#!/usr/bin/python3
# Displays all values in the states table of the database hbtn_0e_0_usa
# whose name matches that supplied as argument.

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    crs = db.cursor()
    crs.execute("SELECT * FROM `states` \
          WHERE `name` = '{}'".format(sys.argv[4]))
    for stat in crs.fetchall():
      print(stat)
