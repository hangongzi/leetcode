# 求x的平方根，精确到精度precision
# 二分查找

def x_sqrt(x: int, precision: float)->float:
    l, r = 0, x
    while l<r:
        mid = l+(r-l)/2.0
        if abs(mid*mid-x)<=precision:
            return mid
        elif mid*mid>x:
            r = mid
        elif mid*mid<x:
            l = mid

    return mid


print(x_sqrt(2, 0.001))
