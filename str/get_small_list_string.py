def getSmallString(n: int, k: int)->str:
    res = [1 for _ in range(n)]
    bound = (k-n)//25
    r = (k-n)%25
    res[n-bound-1] = 1+r
    for i in range(n-bound, n):
        res[i] = 26
    return ''.join(map(lambda x: chr(x+96), res))

print(getSmallString(5, 73))
