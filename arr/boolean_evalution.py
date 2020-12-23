def boolean_evalution(s: str, result: int)->int:
    if not s:
        return 0

    if len(s) == 1:
        return 1 if ord(s)-ord('0') == result else 0

    ch = list(s)
    dp = [[[0]*2 for _ in range(len(ch))] for _ in range(len(ch))]
    for i in range(len(ch)):
        if ch[i] == '1' or ch[i] == '0':
            dp[i][i][ord(ch[i])-ord('0')] = 1

    # 套区间dp模板
    # 枚举区间长度len, 跳步为2, 一个数字一个字符
    for len_ in range(2, len(ch)+1, 2):
        # 枚举区间起步点，数字位
        for i in range(0, len(ch)-len_, 2):
            # 区间终点，数字位
            j = i+len_
            # 枚举分割点，三种符号，跳步为2
            for k in range(i+1, j, 2):
                if ch[k] == '&':
                    dp[i][j][0] += dp[i][k-1][0]*dp[k+1][j][0] + dp[i][k-1][0]*dp[k+1][j][1] * dp[i][k-1][1]*dp[k+1][j][1]
                    dp[i][j][1] += dp[i][k-1][1]*dp[k+1][j][1]
                elif ch[k] == '|':
                    dp[i][j][0] += dp[i][k-1][0]*dp[k+1][j][0]
                    dp[i][j][1] += dp[i][k-1][1]*dp[k+1][j][1]+dp[i][k-1][0]*dp[k+1][j][1]+dp[i][k-1][1]*dp[k+1][j][0]
                elif ch[k] == '^':
                    dp[i][j][0] += dp[i][k-1][0]*dp[k+1][j][0]+dp[i][k-1][1]*dp[k+1][j][1]
                    dp[i][j][1] += dp[i][k-1][0]*dp[k+1][j][1]+dp[i][k-1][1]*dp[k+1][j][0]

    return dp[0][len(ch)-1][result]

print(boolean_evalution("1^0|0|1", 0))
