"""
1. 对插入排序的改进：
    插入排序几乎已经排好序的数据进行操作时效率高，几乎可以达到线性排序的效率
    但是插入排序一般是低效的，因为插入排序每次只能将数据移动一位
2. 将全部元素分为几个区域来提升插入排序的性能，这样就能让一个元素朝最终位置前进一大步。
    然后算法再逐步取越来越小的步长进行排序，算法的最后一步就是插入排序，但是此时数组几乎已经是排好序了。
3. 步长序列：建议最初步长为n/2，然后每次对步长取半，直到步长为1的位置
"""


def shellSort(nums: list):
    n = len(nums)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = nums[i]
            j = i
            while j >= gap and nums[j - gap] > temp:
                nums[j] = nums[j - gap]
                j -= gap
            nums[j] = temp
        gap = gap // 2

    return nums
