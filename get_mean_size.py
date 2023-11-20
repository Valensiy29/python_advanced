



def get_mean_size():
    res = 0
    num_list =[]
    with open('datafile.txt', 'r') as file:
        for i in file:
            for num in i.split():
                if num.isnumeric():
                    num_list.append(int(num))
                    res += int(num)

    return res / len(num_list)

get_mean_size()

