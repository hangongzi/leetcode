class Solution:
    def largestPerimeter(self, A: list) -> int:
        ans = 0
        A.sort()
        for i in range(len(A)-1, 1, -1):
            if A[i-1]+A[i-2]>A[i] and A[i]+A[i-1]+A[i-2]>ans:
                ans = A[i]+A[i-1]+A[i-2]
        return ans

print(Solution().largestPerimeter([2,1,2]))


