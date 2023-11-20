from datetime import datetime
from flask import Flask


app2 = Flask(__name__)


@app2.route('/hello/<username>')
def have_a_nice_day(username):
    time = datetime.today().isoweekday()
    weekdays = {1:'понедельника',2:'вторника',3:'среды',4:'четверга',5:'пятницы',6:'субботы',7:'воскресенья'}
    return f'Привет {username}! Хорошего {weekdays[time]}'


if __name__ == '__main__':
    app2.run()