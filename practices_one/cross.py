def solution(a):
    print(a)
    v = len(a)
    h = len(a[0])
    count = 0
    if h == 1:
        return 0
    for i in range(v):
        for j in range(h):
            hr = a[i].copy()
            vr = [a[x][j] for x in range(v)]
            hr.pop(j)
            vr.pop(i)
            print(hr)
            print(vr)
            complete = vr
            complete.extend(hr)
            if sum(complete) == 0:
                print("equal")
                count += 1
            elif sum([x / (sum(complete) / len(complete)) == 1. for x in complete]) == len(complete):
                print("equal")
                count += 1
            else:
                print("Not equal")
    return count
