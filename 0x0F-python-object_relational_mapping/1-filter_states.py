#!/usr/bin/python3
"""
Use MySQLdb to query a database for states whose names
start with the letter N
"""
import sys
import MySQLdb


username = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]
conn = MySQLdb.connect(host="localhost", port=3306, user=username,
                       passwd=password, db=database, charset="utf8")
cur = conn.cursor()
cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

query_rows = cur.fetchall()
for row in query_rows:
    print(row)

cur.close()
conn.close()

if __name__ == "__main__":
    pass
