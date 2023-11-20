from flask import Flask,request
from typing import List

list_sum = Flask(__name__)


@list_sum.route('/sum_num', methods = ["POST"],)
def sum_num():
    data = request.get_data(as_text=True)
    return data
    # num_list:List[int] = request.args.getlist('number',type = int)
    # res = 0
    # for i in num_list:
    #     res += i
    # return str(res)

if __name__ == '__main__':
    list_sum.run()