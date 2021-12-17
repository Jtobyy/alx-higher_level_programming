#!/usr/bin/python3
"""
displays all values in the states table of hbtn_0e_0_usa where name
matches the argument.
"""

import sys
import MySQLdb


username = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]
search = sys.argv[4]

conn = MySQLdb.connect(host="localhost", port=3306, user=username,
                       passwd=password, db=database, charset="utf8")

cur = conn.cursor()
cur.execute(f"SELECT * FROM states WHERE name = '{search}' ORDER BY id ASC")

query_rows = cur.fetchall()
for row in query_rows:
    print(row)

cur.close()
conn.close()

if __name__ == "__main__":
    pass
