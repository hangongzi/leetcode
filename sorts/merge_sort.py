class Solution:
    def mergeSort(self, nums: list):
        self.reverseSort(nums, 0, len(nums)-1)
        return nums

    def reverseSort(self, nums, left, right):
        if left>= right:
            return

        left1 = left
        right1 = (left+right)//2
        left2 = right1 + 1
        right2 = right

        self.reverseSort(nums, left1, right1)
        self.reverseSort(nums, left2, right2)

        temp = []
        while left1<=right1 and left2<=right2:
            if nums[left1]<nums[left2]:
                temp.append(nums[left1])
                left1 += 1
            else:
                temp.append(nums[left2])
                left2 += 1

        while left1<=right1:
            temp.append(nums[left1])
            left1 += 1
        while left2<=right2:
            temp.append(nums[left2])
            left2 += 1

        for i in range(left, right+1):
            nums[i] = temp[i-left]

Solution().mergeSort([2,5,1,3,6,4])
