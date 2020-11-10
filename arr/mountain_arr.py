class Solution:
    def validMountainArray(self, A: list) -> bool:
        N = len(A)
        i = 0
        while i<N-1 and A[i]<A[i+1]:
            i += 1

        if i == N-1 or i==0:
            return False

        while i<N-1 and A[i]>A[i+1]:
            i += 1

        return i == N-1


print(Solution().validMountainArray([0,1,2,3,4,5,6,7,8,9,0]))
