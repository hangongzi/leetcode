def two_sigle_nums(nums: list):
    t = 0
    for num in nums:
        t = t^num

    t = 1&t
    t1, t2 = [], []
    for num in nums:
        if num&t: t1.append(num)
        else: t2.append(num)

    num1, num2 = 0, 0
    for num in t1:
        num1 = num1^num
    for num in t2:
        num2 = num2^num

    return num1, num2

print(two_sigle_nums([99, 78, 34, 56, 99, 34, 78, 67]))
