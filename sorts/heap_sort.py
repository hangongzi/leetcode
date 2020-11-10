class Solution:
    def build(self, nums, start, end):
        while True:
            child = 2*start+1
            if child>end:
                break
            if child<end and nums[child]<nums[child+1]:
                child += 1

            if nums[start]<nums[child]:
                nums[start], nums[child] = nums[child], nums[start]
                start = child
            else:
                break

    def heapSort(self, nums: list):
        n = len(nums)
        first_root = n//2 - 1
        for root in range(first_root, -1, -1):
            self.build(nums, root, n-1)
        for end in range(n-1, 0, -1):
            nums[0], nums[end] = nums[end], nums[0]
            self.build(nums, 0, end-1)
        return nums
