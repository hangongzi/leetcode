class Solution:
    def threeSum(self, nums: list)->list:
        triplets = []
        nums.sort()
        
        for i in range(len(nums)-2):
### 'cur' - first num in possible triplet
### 'seen' - to keep track of 2sums
### 'used' - to keep track of nums used
            cur, seen, used = nums[i], {}, set()
### Can't get a triplet if the smallest number is postive
            if cur > 0: break
### Ignore numbers that were just looked through
            if i > 0 and cur == nums[i-1]: continue
            for j in range(i+1, len(nums)):
### Only a valid triplet if it is in seen and has not yet been used
                if nums[j] in seen and nums[j] not in used:
                    triplets.append([cur,seen[nums[j]],nums[j]])
                    used.add(nums[j])
                else:
### Record 2sum in 'seen'
                    seen[-(cur+nums[j])] = nums[j]
        return triplets


print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))
