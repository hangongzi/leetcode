class Solution:
    def countPrimes(self, n):
        isPrim = [True]*n
        ans = 0
        for i in range(2, n):
            if isPrim[i]:
                ans += 1
                if i*i<n:
                    for j in range(i*i, n, i):
                        isPrim[j] = False
        return ans

print(Solution().countPrimes(15000))
