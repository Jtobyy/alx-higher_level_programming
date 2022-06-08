#!/usr/bin/python3
"""
This script takes in the name of a state as an argument and lists all
cities of that state, using the database hbtn_0e_4_usa
"""

import sys
import MySQLdb


if __name__ == "__main__":
    """ Uses python MySQLdb to query a database """
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state = sys.argv[4]

    for ch in state:
        if ch == ';':
            break

    else:
        conn = MySQLdb.connect(host="localhost", port=3306, user=username,
                               passwd=password, db=database, charset="utf8")

        cur = conn.cursor()
        cur.execute(f"SELECT cities.name FROM states INNER JOIN cities ON \
        cities.state_id = states.id AND states.name = '{state}' ORDER BY \
        cities.id ASC")

        query_rows = cur.fetchall()

        for row in query_rows:
            print(row[0], end="")
            if row is not query_rows[-1]:
                print(", ", end="")
        print()
        cur.close()
        conn.close()
