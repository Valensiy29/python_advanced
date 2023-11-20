import sqlite3

class Items:
    def __init__(self,name: str,id: str,amount: int)->None:
        self.name = name
        self.id = id
        self.amount = amount


def form()->Items:
    id = input('name of product')
    name = input('description of product')
    amount = input('product count')

    amount_val = int(amount)

    return Items(name=name,id=id,amount=amount)

if __name__ == '__main__':
    with sqlite3.connect('./star_1.db') as conn:
        cursor = conn.cursor()
        new_item = form()
        cursor.execute('''
                INSERT INTO 'cars' (id,name,amount) VAlUES 
                (?,?,?);
                ''', (new_item.name, new_item.id, new_item.amount))