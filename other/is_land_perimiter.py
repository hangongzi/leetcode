class Solution:
    def islandPerimeter(self, grid) -> int:
        ret = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] and (i - 1 < 0 or not grid[i - 1][j]):
                    ret += 1
                if grid[i][j] and (i + 1 == len(grid) or not grid[i + 1][j]):
                    ret += 1
                if grid[i][j] and (j - 1 < 0 or not grid[i][j - 1]):
                    ret += 1
                if grid[i][j] and (j + 1 == len(grid[i]) or not grid[i][j + 1]):
                    ret += 1
        return ret


grid = [
    [0, 1, 0, 0],
    [1, 1, 1, 0],
    [0, 1, 0, 0],
    [1, 1, 0, 0]
]
print(Solution().islandPerimeter(grid))
