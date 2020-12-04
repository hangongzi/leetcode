from functools import reduce

class Solution:
    def minCount(self, coins: list) -> int:
        return reduce(lambda total, x: total + x//2+x%2, coins, 0)
        # for i in coins:
        #     total += i//2 + i%2
        # return total

print(Solution().minCount([2,3,10]))