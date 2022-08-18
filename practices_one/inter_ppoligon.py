def solution(n):
    solution = 0

    for i in range(1,n+1):
        if i == 1:
            solution=1
        else:
            solution += (i * 4) - 4
    return solution


if __name__ == '__main__':
    solution(3)
