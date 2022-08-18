import math
import time
from multiprocessing import Pool


def solution_3(sequence):
    s = len(sequence)
    f = []
    if s == 2:
        return True
    for i in range(s - 1):
        p = sequence[i]
        l = sequence[i + 1]
        if p >= l and i > 0:
            with Pool(2) as p:
                result = p.starmap(check, [[sequence, i], [sequence, i + 1]])
                if not (result[0] or result[1]):
                    f.append(1)
    print(f)
    if sum(f) >= 1:
        return False
    else:
        return True


def check(sequence, i):
    set_c = sequence.copy()
    set_c.pop(i)

    for i in range(len(set_c) - 1):
        pp = set_c[i]
        ll = set_c[i + 1]
        if pp >= ll:
            return False
    return True


def solution_2(sequence):
    droppped = False
    last = prev = min(sequence) - 1
    for elm in sequence:
        if elm <= last:
            if droppped:
                return False
            else:
                droppped = True
            if elm <= prev:
                prev = last
            elif elm >= prev:
                prev = last = elm
        else:
            prev, last = last, elm
    return True


def solution(sequence):
    bad = 0
    s = len(sequence)
    if s==2: return True
    for i in range(1, s):
        if sequence[i] <= sequence[i - 1]:
            bad += 1
            if bad > 1:
                return False
            if i>1 and i<s-1 and sequence[i] <= sequence[i - 2] and sequence[i + 1] <= sequence[i - 1]:
                return False
    return True


if __name__ == '__main__':
    # array = [15, 97, 28, 89, 71, 48, 96, 85, 1, 84, 51, 37, 3, 23, 28, 56, 98, 13, 97, 57, 51, 12, 87, 32, 94, 7, 95, 56, 8, 71, 92, 64, 88, 40, 45, 42, 94, 50, 18, 23, 14, 66, 100, 31, 18, 49, 47, 52, 25, 42, 17, 31, 92, 1, 22, 85, 99, 8, 92, 23, 84, 95, 48, 0, 3, 67, 72, 93, 65, 12, 86, 60, 82, 79, 89, 49, 78, 85, 31, 5, 66, 84, 5, 1, 62, 10, 48, 25, 97, 45, 25, 15, 23, 72, 38, 13, 5, 60, 59, 72, 92, 41, 58, 14, 28, 54, 47, 67, 59, 26, 75, 93, 34, 9, 51, 21, 28, 23, 14, 47, 31, 10, 12, 72, 72, 8, 64, 70, 84, 50, 85, 52, 61, 50, 86, 87, 7, 34, 71, 49, 41, 22, 54, 51, 14, 92, 2, 8, 78, 35, 28, 21, 100, 39, 100, 69, 5, 48, 44, 39, 90, 73, 76, 1, 27, 82, 0, 45, 74, 2, 83, 15, 2, 70, 44, 2, 48, 44, 96, 68, 30, 76, 52, 22, 83, 0, 80, 77, 98, 17, 82, 11, 81, 76, 94, 61, 77, 99, 100, 26, 48, 24, 76, 1, 45, 56, 3, 93, 98, 1, 69, 58, 19, 28, 98, 54, 83, 78, 39, 94, 54, 18, 98, 96, 39, 71, 31, 49, 98, 29, 54, 67, 78, 83, 84, 35, 15, 44, 77, 30, 23, 51, 73, 32, 98, 18, 56, 47, 99, 6, 84, 30, 31, 27, 12, 45, 5, 46, 63, 97, 70, 7, 46, 65, 50, 84, 30, 95, 44, 39, 90, 79, 51, 64, 68, 8, 77, 19, 86, 17, 87, 83, 68, 30, 74, 100, 64, 86, 57, 69, 59, 33, 67, 83, 93, 29, 47, 4, 19, 75, 97, 65, 62, 38, 54, 72, 32, 80, 69, 64, 46, 59, 38, 0, 77, 59, 89, 83, 98, 25, 51, 63, 71, 85, 23, 27, 79, 82, 57, 30, 34, 61, 81, 33, 16, 45, 79, 6, 23, 13, 41, 83, 61, 44, 56, 15, 27, 71, 84, 18, 3, 26, 29, 0, 1, 35, 65, 75, 31, 47, 58, 1, 27, 46, 74, 60, 98, 32, 58, 56, 73, 92, 100, 43, 39, 96, 28, 93, 68, 36, 96, 58, 89, 71, 15, 42, 26, 69, 87, 82, 82, 29, 53, 76, 100, 37, 98, 45, 17, 68, 29, 34, 78, 86, 75, 11, 30, 86, 94, 28, 64, 43, 14, 62, 48, 29, 85, 96, 24, 0, 73, 4, 60, 0, 0, 79, 42, 66, 81, 20, 91, 28, 27, 6, 14, 69, 11, 21, 48, 41, 75, 14, 60, 56, 99, 37, 1, 12, 21, 19, 15, 94, 27, 87, 33, 47, 51, 78, 5, 7, 57, 70, 9, 49, 60, 60, 77, 81, 53, 86, 13, 30, 11, 79, 34, 6, 91, 1, 97, 42, 46, 24, 68, 0, 14, 86, 76, 26, 23, 43, 34, 51, 98, 37, 54, 64, 71, 95, 36, 0, 57, 17, 54, 81, 43, 84, 12, 91, 20, 17, 29, 84, 64, 47, 34, 55, 75, 86, 91, 25, 76, 26, 60, 29, 25, 51, 32, 82, 84, 3, 95, 44, 3, 22, 35, 13, 73, 10, 50, 37, 67, 78, 76, 33, 91, 38, 46, 58, 79, 7, 23, 1, 4, 67, 93, 53, 31, 97, 51, 8, 54, 70, 36, 75, 2, 46, 55, 8, 15, 39, 18, 66, 4, 9, 86, 4, 95, 79, 16, 36, 91, 66, 84, 65, 43, 9, 64, 66, 81, 89, 81, 83, 44, 98, 24, 41, 32, 35, 19, 46, 14, 42, 13, 30, 30, 61, 24, 70, 57, 2, 35, 46, 87, 67, 98, 49, 100, 2, 50, 18, 30, 80, 58, 84, 41, 28, 59, 37, 84, 97, 42, 91, 72, 7, 68, 92, 17, 55, 20, 49, 24, 33, 84, 9, 93, 83, 47, 77, 60, 76, 10, 39, 36, 85, 21, 22, 16, 80, 49, 15, 15, 96, 24, 85, 19, 49, 10, 50, 86, 0, 74, 23, 6, 12, 36, 58, 49, 83, 76, 86, 61, 3, 22, 73, 92, 25, 76, 29, 67, 48, 6, 32, 69, 95, 8, 97, 94, 7, 31, 37, 3, 51, 60, 33, 0, 84, 21, 0, 95, 25, 12, 3, 53, 33, 62, 43, 54, 45, 88, 2, 46, 16, 14, 4, 78, 47, 14, 62, 40, 46, 13, 57, 74, 18, 99, 37, 25, 65, 31, 3, 5, 30, 51, 78, 31, 4, 41, 80, 30, 76, 66, 35, 5, 43, 47, 0, 78, 84, 16, 25, 8, 4, 64, 17, 29, 17, 32, 73, 16, 43, 52, 92, 26, 3, 10, 21, 21, 16, 16, 16, 44, 16, 87, 17, 46, 4, 71, 98, 37, 3, 100, 32, 6, 5, 92, 75, 93, 33, 1, 63, 62, 71, 38, 92, 42, 35, 90, 7, 92, 92, 7, 55, 87, 21, 5, 40, 81, 75, 19, 28, 7, 52, 4, 57, 44, 94, 2, 74, 36, 62, 51, 89, 55, 2, 14, 52, 35, 75, 98, 9, 78, 71, 71, 64, 42, 5, 97, 33, 37, 13, 29, 9, 76, 79, 95, 11, 34, 89, 66, 98, 28, 73, 53, 34, 93, 25, 13, 55, 5, 26, 97, 25, 19, 79, 70, 19, 13, 21, 12, 57, 45, 91, 94, 22, 75, 11, 12, 4, 57, 14, 95, 38, 44, 27, 93, 54, 30, 20, 82, 1, 47, 79, 94, 23, 9, 29, 97, 9, 28, 80, 54, 28, 38, 59, 60, 31, 21, 31, 86, 69, 68, 2, 14, 42, 81, 43, 29, 89, 9, 29, 37, 67, 9, 20, 28, 74, 44, 69, 21, 68, 11, 70, 47, 80, 31, 30, 62, 1, 81, 40, 28, 24, 39, 61, 42, 42, 26, 37, 97, 75, 62, 68, 30, 22, 100, 22, 39, 66, 17, 98, 0, 92, 32, 7, 79, 93, 17, 89, 54, 88, 58, 9, 88, 73, 36, 71, 65, 61, 56, 98, 4, 19, 88, 46, 100, 16, 0, 49, 79, 92]
    # solution(array)
    t1 = time.time()
    solution([3, 5, 67, 98, 3])
    t2 = time.time() - t1
    t1 = time.time()
    solution_2([3, 5, 67, 98, 3])
    t3 = time.time() - t1
    print(t2)
    print(t3)
    print(f'Mine Better: {t2 < t3}')
