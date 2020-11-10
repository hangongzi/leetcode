class Solution:
    def kClosest(self, points: list, K: int) -> list:
        points.sort(key=lambda x:x[0]**2+x[1]**2)
        return points[:K]


print(Solution().kClosest(points=[[1,3],[-2,2]], K=1))