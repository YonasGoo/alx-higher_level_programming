#!/usr/bin/python3
# gets all states via python yee boi

import sys
import MySQLdb

def main(args):
    # gets all state stuff
    if len(args) != 4:
        print("Usage: {} username password database".format(args[0]))
        sys.exit(1)

    try:
        db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=args[1],
            passwd=args[2],
            db=args[3]
        )
        
        cur = db.cursor()
        cur.execute("SELECT * FROM states ORDER BY id ASC")
        states = cur.fetchall()
        for state in states:
            print(state)

    except MySQLdb.Error as e:
        print("Error {}: {}".format(e.args[0], e.args[1]))

    finally:
        if cur:
            cur.close()
        if db:
            db.close()

if __name__ == "__main__":
    main(sys.argv)
