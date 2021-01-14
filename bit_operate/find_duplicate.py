from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0

        bit_max = 31
        while not ((n-1)>>bit_max):
            bit_max -= 1
        for bit in range(bit_max+1):
            x = y = 0
            for i in range(n):
                if nums[i] & (1<<bit):
                    x += 1
                if i>=1 and (i&(1<<bit)):
                    y += 1
            if x>y:
                ans |= 1<<bit
        return ans

        # 弗洛伊德环
        # slow, fast = nums[0], nums[nums[0]]
        # while slow!=fast:
        #     slow = nums[slow]
        #     fast = nums[nums[fast]]

        # slow = 0
        # while slow!=fast:
        #     slow = nums[slow]
        #     fast = nums[fast]
        # return slow


print(Solution().findDuplicate([1,2,3,4,4,5,6,7,8]))


