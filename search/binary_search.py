# 属于有序查找算法
def binary_search(nums: list, target: int)->int:
    l = 0
    r = len(nums)-1
    mid = (l+r)//2
    while l<=r:
        if target<nums[mid]:
            r = mid-1
        elif target>nums[mid]:
            l = mid+1
        else:
            return mid
        mid = (l+r)//2

    return -1
