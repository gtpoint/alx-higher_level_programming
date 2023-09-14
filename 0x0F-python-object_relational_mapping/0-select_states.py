#!/usr/bin/python3
# Lists all states from the database hbtn_0e_0_usa.

import sys
from MySQLdb import _mysql

if __name__ == "__main__":
  db=_mysql.connect(host="localhost",user=sys.argv[1],
                  password=sys.argv[2],database=sys.argv[3])
  cursor = db.cursor()
  cursor.execute("SELECT * FROM `states`")
  for stat in cursor.fetchall():
    print(stat)
