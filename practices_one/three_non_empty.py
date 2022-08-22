def solution(s):
    array =  [[True,False,False],
              [True,True,False],
              [False,False,False]]
    import numpy as np

    [2 if len(array[0])==0 else 2 for x in range(1,2)]

    count = 0
    si = len(s)

    combinations = [[s[0:i],s[i:j+1],s[j+1:len(s)]] for i in list(range(1,si-1)) for j in list(range(i,si-1))]
    ##abc = [[item[0]+item[1],item[1]+item[2],item[2]+item[0]] for item in combinations]
    are_the_same = [True if item[0]+item[1]!=item[1]+item[2]
                            and item[1]+item[2]!=item[2]+item[0]
                            and item[2]+item[0]!=item[0]+item[1]  else False for item in combinations]

    # for i in range(1,len(s)-1):
    #     for j in range(i,len(s)-1):
    #         count+=1
    #         a = s[0:i]
    #         b = s[i:j+1]
    #         c = s[j+1:len(s)]
    #         print(f'a+b: {a+b} \t b+c: {b+c} \t c+a: {c+a}')
    #         if a+b != b+c != c+a != a+b:
    #             count += 1

    return sum(are_the_same)
