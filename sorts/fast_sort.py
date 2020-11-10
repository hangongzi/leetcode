"""
原理：
选择一个基准，将比它小的放在该基准的左侧，将比它大的放在该基准的右侧，然后再分别对左右两个子数组也进行同样的操作，直到数组有序为止。
步骤：
1。 用一个基准数将数组分割成两个子数组
2。 将大于基准数的数移到其右侧，将由于基准数的移到其左侧
3。 递归的进行以上两个步骤，直到整个数组有序
"""


def fastSort(nums: list, low: int, high: int) -> list:
    if low < high:
        # 获取一次区间划分的中间索引pi，pi的左侧已经全部小于nums[pi]
        pi = partition(nums, low, high)
        # 对做区间进一步划分
        fastSort(nums, low, pi - 1)
        # 对右区间进一步划分
        fastSort(nums, pi + 1, high)
    return nums


def partition(arr: list, low: int, high: int):
    # 获取最低位的前一位
    i = (low - 1)
    # 将最高位作为基准
    pivot = arr[high]

    # 遍历从最低位到最高位的前一位
    for j in range(low, high):
        # 与基准比较，如果小于基准，则整体不动（因为基准本身是最高位）。如果大于基准，则索引继续向前
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    # 将第一个大于基准的数与基准交换，然后返回这个值的索引，作为下次递归的边界（保正了这个索引左侧的部分全部小于这个值）
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
