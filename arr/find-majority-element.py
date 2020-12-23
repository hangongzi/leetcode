from typing import List
from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        t = Counter(nums)
        majority = max(t.items(), key=lambda x: x[1])
        
        return majority[0] if majority[1]>len(nums)//2 else -1


print(Solution().majorityElement([3,2]))
