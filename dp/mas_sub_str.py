def maxSubStr(s: str):
    if not s:
        return s
    # 双指针
    # p1, p2 = 0, 1
    # ans = []
    # for i in range(1, len(s)):
    #     if i and int(s[i-1])+1 == int(s[i]):
    #         p2 = i+1
    #     else:
    #         ans.append(s[p1: p2])
    #         p1, p2 = i, i+1
    # ans.append(s[p1: p2])

    # return max(ans, key=lambda x: len(x))

    # 动态规划
    # dp = [0]*len(s)
    # for i in range(len(s)):
    #     if i == 0:
    #         dp[i] = s[0]
    #     elif int(s[i-1])+1==int(s[i]):
    #         dp[i] = dp[i-1]+s[i]
    #     else:
    #         dp[i] = s[i]

    # return max(dp, key=lambda x: len(x))
    # max_len = max(dp)
    # max_idx = dp.index(max_len)
    # ans = []
    # for i in range(max_idx, max_idx-max_len-1, -1):
    #     ans.append(s[i])
    # return ''.join(ans[::-1])

print(maxSubStr('1234563453456789'))

