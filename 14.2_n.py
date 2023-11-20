from flask import Flask
import sqlite3
from python_advanced_2.mail import mail_count
from names import author
app = Flask(__name__)

@app.route('/books')
def return_count():
    return mail_count()

@app.route('/search')
def author_search(name):
    return author(name)

if __name__ == '__main__':
    app.run()
