import sys

from flask import Flask


app3 = Flask(__name__)


@app3.route('/max_number/<path:numbers>')
def max_num(numbers):
    print(str(max(int(i) for i in numbers.split('/'))), file=sys.stderr)


if __name__ == '__main__':
    app3.run()