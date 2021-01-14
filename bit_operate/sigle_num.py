def sigle_num(nums: list):
    seen_once, seen_two = 0, 0
    for num in nums:
        seen_once = ~seen_two&(seen_once^num)
        seen_two = ~seen_once&(seen_two^num)

    return seen_once

print(sigle_num([2,2,3,2]))

