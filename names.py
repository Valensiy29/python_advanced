import sqlite3

name = input('author name is:')

def author(name):
    with sqlite3.connect('home_work/boxers.db') as conn:
        c = conn.cursor()
        c.execute('''
        SELECT mounth FROM 'mails' WHERE mounth = name
        ''')
        res = c.fetchall()
        print(res)

if __name__ == '__main__':
    author(name)

