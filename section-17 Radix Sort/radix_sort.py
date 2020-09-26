def get_max_digit_count(array):
    return len(str(int(max([abs(x) for x in array]))))

def get_digit(number, index_for_digit):
    try:
        if number>=0:
            return int(str(int(abs(number)))[-1-index_for_digit])
        else:
            return -int(str(int(abs(number)))[-1-index_for_digit])
    except Exception:
        return 0

def radix_sort(array):
    buckets = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
    for index in range(get_max_digit_count(array)):
        for number in array:
            digit = get_digit(number, index)
            buckets[9 + digit].append(number)

        array = []
        for bucket in buckets:
            for num in bucket:
                array.append(num)
        buckets = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]

        
    return array




from copy import deepcopy

import random,time

rand_arr = [random.randint(-1000,1000) for x in range(1000)]

radix_sort(deepcopy(rand_arr))