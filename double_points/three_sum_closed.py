class Solution:
    def threeSumClosest(self, nums: list, target: int) -> int:
        nums.sort()
        ans = None
        for idx in range(len(nums)):
            l_p = idx+1
            r_p = len(nums)-1
            while l_p<r_p:
                tmp = nums[idx]+nums[l_p]+nums[r_p]
                if tmp==target:
                    return target
                if tmp<=target:
                    ans = tmp if ans is None or abs(target-tmp)<abs(target-ans) else ans
                    l_p += 1
                elif tmp>target:
                    ans = tmp if ans is None or abs(target-tmp)<abs(target-ans) else ans
                    r_p -= 1
        return ans

print(Solution().threeSumClosest([-1,2,1,-4], 1))