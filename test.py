import time


def task(number):
    start = time.time()
    ex = sum(i ** i for i in range(number))
    res = time.time() - start
    return ex,res

def task1(number):
    start = time.time()
    ex = sum(i ** i for i in range(number))
    res = time.time() - start
    return ex,res

def task2(number):
    start = time.time()
    ex = sum(i ** i for i in range(number))
    res = time.time() - start
    return ex,res

def task3(number):
    start = time.time()
    ex = sum(i ** i for i in range(number))
    res = time.time() - start
    return ex,res

def task4(number):
    start = time.time()
    ex = sum(i ** i for i in range(number))
    res = time.time() - start
    return ex,res
number = 500
task(number)
task1(number)
task2(number)
task3(number)
task4(number)