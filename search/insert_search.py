# 基本思想：基于二分查找算法，将查找点的选择改进为自适应选择，可以提高查找效率。当然，差值查找也属于有序查找。
import math

def insert_search(nums: list, target: int)->int:
    return help_func(nums, 0, len(nums)-1, target)

def help_func(nums, l, r, target):
    mid = l + math.floor((target-nums[l])/(nums[r]-nums[l])*(r-l))
    if nums[mid]==target:
        return mid
    if nums[mid]>target:
        return help_func(nums, mid+1, r, target)
    if nums[mid]<target:
        return help_func(nums, l, mid-1, target)

