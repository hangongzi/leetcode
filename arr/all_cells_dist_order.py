class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int)->list:
        ret = [[i, j] for i in range(R) for j in range(C)]
        ret.sort(key=lambda x: abs(x[0]-r0)+abs(x[1]-c0))
        return ret

print(Solution().allCellsDistOrder(2, 3, 1, 2))
a = [1,2]
a.index(1)