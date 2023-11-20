from flask import Flask
import csv
import logging

app = Flask(__name__)


@app.route('/bank_api/<branch>/<int:person_id>')
def bank_api(branch:str,person_id:int):
    branch_card_file_name = f'bank_data/{branch}.csv'
    with open(branch_card_file_name,'r') as fi:
        csv_reader = csv.DictReader(fi,delimetr=',')
        for record in csv_reader:
            if int(record['id']) == person_id:
                return record['name']
        else:
            return 'Person not found',404





if __name__ == '__main__':
    app.run()