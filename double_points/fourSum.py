class Solution:
    def fourSum(self, nums: list, target: int)->list:
        def kSum(nums: list, target: int, k: int)->list:
            if len(nums)==0 or nums[0]*k>target or nums[-1]*k<target:
                return []
            if k==2:
                return twoSum(nums, target)

            ans = []
            for i in range(len(nums)):
                if i==0 or nums[i-1]!=nums[i]:
                    for _, set in enumerate(kSum(nums[i+1:], target-nums[i], k-1)):
                        ans.append([nums[i]]+set)
            return ans


        def twoSum(nums: list, target: int)->list:
            ans = []
            s = set()
            for i in range(len(nums)):
                if len(ans) == 0 or ans[-1][1] != nums[i]:
                    if target-nums[i] in s:
                        ans.append([target-nums[i], nums[i]])
                s.add(nums[i])

            return ans
        nums.sort()
        return kSum(nums, target, 4)

    

print(Solution().fourSum([1, 0, -1, 0, -2, 2], 0))
