import sqlite3 as sl

con = sl.connect('star_1.db')

with con:
    con.execute("""CREATE TABLE goods (
           product VARCHAR(20) PRIMARY KEY,
           count INTEGER,
           price INTEGER

);
    """)

