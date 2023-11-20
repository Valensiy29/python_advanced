def summary_file():
    with open('output.txt', 'r') as file:
        for i in file:
            word = i.split()
            num_list = [int(num) for num in filter(
                lambda num: num.isnumeric(), word)]
            for i in num_list:
                res = i / 1000
                print(res)


summary_file()