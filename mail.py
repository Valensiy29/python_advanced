import sqlite3


def mail_count():
    with sqlite3.connect('home_work/boxers.db') as conn:
        c = conn.cursor()
        c.execute('''
        SELECT COUNT(mounth) FROM 'mails'
        ''')
        res = c.fetchall()
        print(res)

if __name__ == '__main__':
    mail_count()
