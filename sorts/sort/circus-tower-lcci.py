from typing import List
import bisect


class Solution:
    def bestSeqAtIndex(self, height: List[int], weight: List[int]) -> int:
        dp = []
        for a, b in sorted(zip(height, weight), key=lambda x: [x[0], -x[1]]):
            pos = bisect.bisect_left(dp, b)
            dp[pos:pos+1] = [b]
        return len(dp)
        # peples = list(zip(height, weight))
        # n = len(peples)
        # # sort with height
        # peples.sort(key=lambda x: x[0])
        # for i in range(1, n):
        #     if peples[i][0] == peples[i-1][0] and peples[i][1] > peples[i-1][1]:
        #             peples[i], peples[i-1] = peples[i-1], peples[i]
        # dp = [0]*n
        # res = 0
        # for p in peples:
        #     i, j = 0, res
        #     while i<j:
        #         mid = i+(j-i)//2
        #         if dp[mid]<p[1]: i = mid+1
        #         else: j = mid
        #     dp[i] = p[1]
        #     if res == j: res += 1

        # return res

print(Solution().bestSeqAtIndex([58,65,70,56,75,60,68], [108, 100,150,90,190,95,110]))
