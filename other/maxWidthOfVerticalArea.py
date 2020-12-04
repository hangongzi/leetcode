class Solution:
    def maxWidthOfVerticalArea(self, points: list) -> int:
        points.sort(key=lambda x: x[0])
        return max(p2[0]-p1[0] for p1, p2 in zip(points, points[1:]))


print(Solution().maxWidthOfVerticalArea([[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]))
