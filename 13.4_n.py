import sqlite3

def transfer(c: sqlite3.Cursor):
    sq = c.execute('''INSERT INTO mails (mounth, text)
SELECT mounth, text
FROM table_june
''')


if __name__ == '__main__':
    with sqlite3.connect('boxers.db') as conn:
        c = conn.cursor()

        c.execute('''
            CREATE TABLE IF NOT EXISTS mails (
                mounth TEXT,
                text REAL
            );
        ''')
        transfer(c)
