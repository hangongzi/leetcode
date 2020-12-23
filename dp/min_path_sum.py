import numpy as np

def minPathSum(grid):
    dp = np.zeros((len(grid), len(grid[0])), dtype=np.int32)
    dp[0, 0] = grid[0][0]
    for i in range(1, len(grid[0])):
        dp[0, i] = dp[0, i-1]+grid[0][i]

    for i in range(1, len(grid)):
        dp[i, 0] = dp[i-1, 0] + grid[i][0]

    for i in range(1, len(grid)):
        for j in range(1, len(grid[0])):
            dp[i][j] = min(dp[i-1, j], dp[i, j-1])+grid[i][j]

    return dp[-1, -1]


grid = [
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
]
print(minPathSum(grid))
