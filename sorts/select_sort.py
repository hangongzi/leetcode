# 每次从未排序的数组中找出最小的元素，放到有序数组的末尾（乱序数组的头部），最终实现整个数组都有序排列
# 1. 首先从未排序序列中找到最小元素，将其放到排序序列的起始位置
# 2. 再从剩余未排序元素中寻找最小元素，然后放到已排序序列的末尾
# 3. 重复以上过程，直到所有元素都排序完毕
def selectSort(nums: list):
    for i in range(len(nums)):
        min_num = min(nums[i:])
        index = nums.index(min_num)
        nums[i], nums[index] = min_num, nums[i]
    return nums


