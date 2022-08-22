class Solution:
    def countPrimes(self, n: int) -> int:
        #n=3
        count = 0
        if n in [0,1,2]:
            return 0
        else:
            for i in range(3,n+1):
                if n==1:
                    continue
                is_print=True
                print(f'i: {i // 2 + 1} Range to check: {list(range(2, i // 2 + 1))}')

                for j in range(2, i // 2 + 1):
                    if (i % j == 0):
                        is_prime = False
                        break
                if is_print:
                    count=count+1
                print(f'i:{i} c:{count}')
        print(f'count : {count}')
        return count