#!/usr/bin/python3
"""
Use MySQLdb to query a database for states whose names
start with the letter N
"""
import sys
import MySQLdb


if __name__ == "__main__":
    """ Uses python MySQLdb to query a database """
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    conn = MySQLdb.connect(host="localhost", port=3306, user=username,
                           passwd=password, db=database, charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' OR name LIKE 'n%' \
    ORDER BY id ASC")

    query_rows = cur.fetchall()
    for row in query_rows:
        print("({}, '{}')".format(row[0], row[1]))

    cur.close()
    conn.close()
