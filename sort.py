import heapq
import json
import logging
from typing import List
from flask import Flask, request
import time

app = Flask(__name__)
logger = logging.getLogger("sort")


def bubble_sort(array: List[int]) -> List[int]:
    backtime = time.time()
    n = len(array)
    for i in range(n):
        for j in range(i + 1, n):
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
                return array
    nowtime = time.time()
    res = nowtime - backtime
    logger.debug(res)



def tim_sort(array: List[int]) -> List[int]:
    backtime = time.time()
    array.sort()
    nowtime = time.time()
    res = nowtime - backtime
    logger.debug(res)
    return array


def heap_sort(array: List[int]) -> List[int]:
    backtime = time.time()
    data = []
    for val in array:
        heapq.heappush(data, val)
        return [heapq.heappop(data) for _ in range(len(data))]
    nowtime = time.time()
    res = nowtime - backtime
    logger.debug(res)


algorithms = {
    "bubble": bubble_sort,
    "tim": tim_sort,
    "heap": heap_sort,
    }

@app.route("/<algorithm_name>/", methods=["POST"])
def sort_endpoint(algorithm_name: str):
    if algorithm_name not in algorithms:
        return f"Bad algorithm name, acceptable values are {algorithms.keys()}", 400
    form_data = request.get_data(as_text=True)
    array = json.loads(form_data)
    result = algorithms[algorithm_name](array)
    return json.dumps(result)


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    logger.info("Started sort server")
    app.config["WTF_CSRF_ENABLED"] = False
    app.run(debug=True)