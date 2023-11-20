import sqlite3


if __name__ == '__main__':
    with sqlite3.connect('python_advanced_2/home_work/star_1.db') as conn:
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM 'goods'")

        result = cursor.fetchall()

        print(result)