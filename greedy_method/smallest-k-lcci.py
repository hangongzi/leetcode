class Solution:
    def smallestK(self, arr: list, k: int) ->list:
        def partition(start, end):
            p = arr[end]
            j = start - 1
            for i in range(start, end):
                if arr[i]<p:
                    j += 1
                    arr[i], arr[j] = arr[j], arr[i]
            arr[j+1], arr[end] = arr[end], arr[j+1]
            return j+1
        # def partition(start, end):
        #     piovt = start
        #     l = start + 1
        #     r = end
        #     while True:
        #         while l<=r and arr[l]<arr[piovt]: l += 1
        #         while r>=l and arr[r]>arr[piovt]: r -= 1
        #         if l>r:
        #             break
        #         arr[l], arr[r] = arr[r], arr[l]
        #         l += 1
        #         r -= 1
        #     arr[piovt], arr[r] = arr[r], arr[piovt]
        #     return r

        start, end = 0, len(arr)-1
        if k>len(arr) or k<=0:
            return []
        else:
            while True:
                p = partition(start, end)
                if p==k:
                    break
                if p>k:
                    end = p-1
                elif p<k:
                    start = p+1

        return arr[:k]


# 堆
# def shift_heap(arr, start, end):
#     root = start
#     while True:
#         child = 2 * root + 1
#         if child > end:
#             break
#         if child + 1 <= end and arr[child] < arr[child + 1]:
#             child += 1
#         if arr[root] < arr[child]:
#             arr[root], arr[child] = arr[child], arr[root]
#             root = child
#         else:
#             break


# def find_kth_nums(arr, k):
#     if k > len(arr):
#         return arr
#     heap_t = arr[:k]
#     for start in range(len(heap_t)//2-1, -1, -1):
#         shift_heap(heap_t, start, len(heap_t)-1)

#     for i in arr[k:]:
#         if i<heap_t[0]:
#             heap_t[0] = i
#             shift_heap(heap_t, 0, len(heap_t)-1)

#     return heap_t

print(Solution().smallestK([1,3,5,7,2,4,6,8], 4))
