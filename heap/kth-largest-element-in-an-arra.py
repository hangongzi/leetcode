import random

class Solution(object):
    def findKthLargest(self, nums, k):
        nums.sort(reverse=True)
        return nums[k-1]
        # 快速排序解法
        # def partition(start, end):
        #     key = nums[end]
        #     j = start -1
        #     for i in range(start, end):
        #         if nums[i]<=key:
        #             j += 1
        #             nums[j], nums[i] = nums[i], nums[j]
        #     nums[j+1], nums[end] = nums[end], nums[j+1]
        #     return j+1

        # def randomPartition(start, end):
        #     i = random.randint(start, end+1)
        #     nums[i], nums[end] = nums[end], nums[i]
        #     return partition(start, end)

        # def quickSelect(start, end, idx):
        #     q = randomPartition(start, end)
        #     if q == idx:
        #         return nums[q]
        #     else:
        #         return quickSelect(q+1, end, idx) if q<idx else quickSelect(start, q-1, idx)

        # return quickSelect(start=0, end=len(nums)-1, idx=k)

        # 堆
        # def shift_heap(start, end):
        #     root = start
        #     while True:
        #         child = 2*root+1
        #         if child>end:
        #             break
        #         if child+1<=end and nums[child]<nums[child+1]:
        #             child = child + 1
        #         if nums[root]<nums[child]:
        #             nums[root], nums[child] = nums[child], nums[root]
        #             root = child
        #         else:
        #             break

        # n = len(nums)

        # for start in range(n//2-1, -1, -1):
        #     shift_heap(start, n-1)

        # for end in range(n-1, n-k, -1):
        #     nums[0], nums[end] = nums[end], nums[0]
        #     shift_heap(0, end-1)

        # return nums[0]

print(Solution().findKthLargest([3,2,1,5,6,4], 2))
