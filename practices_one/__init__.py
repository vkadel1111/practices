import matplotlib.pyplot as plt
import numpy
import numpy as np


def sub_lists(l):
    lists = []
    for i in range(len(l) + 1):
        for j in range(i):
            lists.append(l[j: i])
    return lists

def leet_problem_1524(arr):
    from itertools import chain, combinations
    # [[1],[1,3],[1,3,5],[3],[3,5],[5]]
    # [1,4,9,3,8,5]
    # [1, *2, 3, *4, 5, *6, 7]
    # [-1, -3, 6, 10, -15, -21, 28]
    # 4 = 10 2.5
    # 5 = 15 3
    # 6 = 21 3.5
    # 7 = 28 4
    # 8 = 36 4.5
    # 9 = 45 5
    # result / e_count = ratio = e_count/2 + .5
    e_count = len(arr)
    comb_number = int(((e_count/2) + 1/2) * e_count)

    sub_list=sub_lists(arr)
    summs = numpy.array([sum(x) for x in sub_list])
    odds_list = summs[summs%2!=0]
    even_list = summs[summs%2==0]
    cum_sum = np.cumsum(arr)
    cumSum = odd = even = 0
    for num in arr:
        cumSum += num
        if cumSum % 2:
            odd += 1
        else:
            even += 1
    ## 1 odd 4 even 5 cumsum 10 even 4+1*2 1-1
    ## 5 odd 1 even 6 cumsum 11 even 5+1*2 1-1
    ## 6 odd 1 even 7 sumcum 16 even 6+1*2 1-1
    ## 5 odd 2 even 7 sumcum 13 even 5+1*2 2-1
    ## 3 odd 4 even 7 sumcum 13 even 5+1*2 2-1

    even_cal = odd * even + (even - odd)
    return odd * (even + 1) % (pow(10, 9) + 7)


def let_1524():
    arr = [1, 3, 5]

def initial_code():
    print('Module practice_one')
    import heapq
    import numpy as np
    import seaborn as sn
    heap_size = 10
    t_list = np.random.randint(1, 520, heap_size)
    unorg = t_list.tolist()
    heapq.heapify(unorg)
    _, ax = plt.subplots(2, 1)
    sn.barplot(np.arange(1, heap_size + 1), t_list, ax=ax[0])
    sn.barplot(np.arange(1, heap_size + 1), unorg, ax=ax[1])
    plt.show()


def let_1491(salaries):
    salaries.sort()
    salaries.pop(0)
    salaries.pop(len(salaries) - 1)
    import statistics
    av = statistics.mean(salaries)

def leet_1523(low, high):
    # Sn = n/2 × [a + l]
    #
    import numpy as np
    i = 0
    my_set = np.arange(low, high + 1)
    s = my_set[my_set % 2 != 0]
    result = int((high - low + low % 2 + high % 2) / 2)

if __name__ == '__main__':
    print("starting")
    number=leet_problem_1524([1,9,4,6,7,3,5])
    number=leet_problem_1524([2,4,6,10,3,8,6,4,3,1])
    number=leet_problem_1524([1, 2, 3, 4, 5, 6, 7])
    number=leet_problem_1524([1, 3, 5])


    let_1491(list([4000, 3000, 1000, 2000]))
    leet_1523(10, 99)
    # initial_code()
