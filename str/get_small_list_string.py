def getSmallString(n: int, k: int)->str:
    ans = []

    

    ans = ''.join(map(lambda x: chr(x+96), ans[::-1]))
    return ans

print(getSmallString(5, 31))
