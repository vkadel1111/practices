
def solution1(inputString):
    if len(inputString)==1:
        return True
    else:
        i = 0
        j = len(inputString)-1
        while i < len(inputString)-1 and j > 0:
            if inputString[i]==inputString[j]:
                i += 1
                j -= 1
            else:
                return False
        return True
def solution(inputArray):
    s = len(inputArray)
    if s==0:
        return 0
    elif s==1:
        return inputArray[0]
    elif s==2:
        return inputArray[0]*inputArray[1]
    elif s > 2 :
        cu_m = inputArray[0]*inputArray[1]
        n_cu = inputArray[1]*inputArray[2]
        for i in range(2,s-1):
            if n_cu > cu_m:
                cu_m = n_cu
            n_cu =  inputArray[i]*inputArray[i+1]
        return max(cu_m,n_cu)

if __name__ == '__main__':

    solution([3, 6, -2, -5, 7, 3])
    # solution1("aabaa")