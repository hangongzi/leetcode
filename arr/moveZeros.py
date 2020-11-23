def test(x):
    if x<=0 or (x>=10 and x%10==0):
        return False
    t = 0
    while t<x:
        t = t*10+x%10
        x = x//10
    return t==x or t==(x*10+t%10)


print(test(0))
