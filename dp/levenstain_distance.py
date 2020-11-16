import numpy as np

def lev(s1: str, s2: str)->int:
    dp = np.zeros((len(s1)+1, len(s2)+1), dtype=np.int)
    dp[0] = np.arange(len(s2)+1)
    dp[:, 0] = np.arange(len(s1)+1)

    for i in range(1, len(s1)+1):
        for j in range(1, len(s2)+1):
            d1 = dp[i-1, j]+1
            d2 = dp[i, j-1]+1
            d3 = dp[i-1, j-1]+(1 if s1[i-1] != s2[j-1] else 0)
            dp[i, j] = np.min([d1, d2, d3])

    return dp[-1, -1]


print(lev('love', 'lolpe'))
