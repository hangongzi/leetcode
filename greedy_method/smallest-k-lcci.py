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


print(Solution().smallestK([1,3,5,7,2,4,6,8], 4))
