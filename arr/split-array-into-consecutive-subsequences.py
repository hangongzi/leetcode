from collections import defaultdict
import heapq

# mp: key为nums数字，value为key对应的可以组成的子数组长度
# queue：用于临时存储x-1的最小堆


class Solution:
    def isPossible(self, nums: list) -> bool:
        mp = defaultdict(list)
        for x in nums:
            if queue := mp.get(x - 1):
                # 每次取子数组长度最小值进行重组
                prevLength = heapq.heappop(queue)
                heapq.heappush(mp[x], prevLength + 1)
            else:
                # 如果不存在x-1的数字，则新建数组
                heapq.heappush(mp[x], 1)
        
        return not any(queue and queue[0] < 3 for queue in mp.values())

print(Solution().isPossible([1,2,3,3,4,5]))
