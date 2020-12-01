from heapq import heappush, heappop
import math


class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        # 动态规划
        dp = [1, ]*n
        idxs = [0]*len(primes)
        
        for i in range(1, n):
            min_num = math.inf
            for idx, prime in enumerate(primes):
                if min_num>dp[idxs[idx]]*prime:
                    min_num = dp[idxs[idx]]*prime
            dp[i] = min_num

            for j in range(len(primes)):
                if min_num==dp[idxs[j]]*primes[j]:
                    idxs[j] += 1

        return dp[n-1]


        # 堆
        # heap = []
        # heappush(heap, 1)
        # seen = {1, }
        # for i in range(1, n):
        #     ugly_num = heappop(heap)
        #     for j in primes:
        #         new_ugly = ugly_num*j
        #         if new_ugly not in seen:
        #             seen.add(new_ugly)
        #             heappush(heap, new_ugly)
        # return heappop(heap)

print(Solution().nthSuperUglyNumber(12, [2,7,13,19]))
