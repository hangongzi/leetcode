"""
桶排序以下列程序进行：

设置一个定量的阵列当作空桶子。
寻访序列，并且把项目一个一个放到对应的桶子去。
对每个不是空的桶子进行排序。
从不是空的桶子里把项目再放回原来的序列中。

每隔桶存储相同数值区间的数，大致做了排序
每个桶再次排序
将每个桶的数重新放回，最终有序
"""


class Solutino:
    def bucketSort(self, nums: list):
        max_num, min_num = max(nums), min(nums)
        bucketNum = max_num//10-min_num//10+1
        bucketList = [[]*bucketNum]
        for i in range(len(nums)):
            index = self.indexFor(nums[i], min_num, 10)
            bucketList[index].append(nums[i])

        index = 0
        for i in range(bucketNum):
            bucket = bucketList[i]
            self.insertSort(bucket)
            for num in bucket:
                nums[index] = num
                index += 1
        return nums

    def indexFor(self, a, min, step):
        return (a-min)//step

    def insertSort(self, arr):
        for i in range(len(arr)):
            key = arr[i]
            j = i-1
            while j>=0 and key<arr[j]:
                arr[j+1] = arr[j]
                j -= 1
            arr[j+1] = key

print(Solutino().bucketSort([2,3,1,6,4,5]))