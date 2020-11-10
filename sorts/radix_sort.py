"""
原理：
基数排序是一种非比较型整数排序算法，其原理是将整数按照位数切割成不同的数字，然后按照每个位数进行比较。
步骤：
1. 获取数组a中的最大值，并用其计算数组的最大指数
2. 从指数1开始，根据位数对应数组中的数字进行桶排序
3. 对数组a按照指数进行排序
"""
class Solution:
    def radixSort(self, nums:list):
        