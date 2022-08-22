def solution(m):
    v = len(m)
    h = len(m[0])
    r = m.copy()
    j = 1
    # print(m[1][j-1:j+1])
    # print(list(range(v)))
    l = [m[i:i + 2] if i == 0
         else m[i - 1:i + 2] if 0 < i < v
    else m[i - 1:i + 2] if i == v - 1
    else 0 for i in range(v)]

    print(f'test:{[e[0:2] for e in l[1]]}')

    print(
        [
            k[i][0:j + 2] if j == 0
            else k[i][j - 1:j + 1] if 0 < j < h - 1
            else k[i][j - 1:j + 1] if j == h - 1
            else 0 for k in l for i in range(len(l) - 1) for j in range(h)
        ]
    )

    # print(r)
    return (r)
    # k[i][0:j+2] if j==0
    # else k[i][j-1:j+1] if 0<j<h-1
    # else k[i][j-1:j+1] if j==h-1
    # else 0
