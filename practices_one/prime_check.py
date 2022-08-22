class Solution:

    def countPrimes(self, n: int) -> int:

        # n=3
        count = 0
        if n in [0, 1, 2]:
            return 0
        else:
            for i in range(3, n + 1):
                if n == 1:
                    continue
                if self.isPrime(self,i):
                    count = count + 1
                print(f'i:{i} c:{count}')
        print(f'count : {count}')
        return count

    def isPrime(self, n):
        for j in range(2, n // 2 + 1):
            if (n % j == 0):
                return False
        return True

