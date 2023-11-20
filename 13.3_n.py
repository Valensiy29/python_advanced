import sqlite3


def delete_boxers(c:sqlite3.Cursor):
    c.execute('''DELETE FROM 'boxers' WHERE name LIKE 'Майк%' ''')


if __name__ == '__main__':
    conn = sqlite3.connect('boxers.db')
    c = conn.cursor()

    c.execute('''
        CREATE TABLE IF NOT EXISTS boxers (
            name TEXT,
            height REAL,
            weight REAL
        );
    ''')

    def add_boxer(name, height, weight):
        c.executescript(f"INSERT INTO boxers VALUES ('{name}', '{height}', '{weight}');")

    add_boxer('Майк Тайсон', 178, 118)
    add_boxer('Мохаммед Али', 193, 102)
    # ... и так далее. Добавьте ещё 19 пар имя-параметры роста и веса.
    delete_boxers(c)
    conn.commit()
    conn.close()

