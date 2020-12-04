from collections import defaultdict
import heapq

class Solution:
    def isPossible(self, nums: list) -> bool:
        mp = defaultdict(list)
        for x in nums:
            if queue := mp.get(x - 1):
                prevLength = heapq.heappop(queue)
                heapq.heappush(mp[x], prevLength + 1)
            else:
                heapq.heappush(mp[x], 1)
        
        return not any(queue and queue[0] < 3 for queue in mp.values())

print(Solution().isPossible([1,2,3,3,4,5]))
