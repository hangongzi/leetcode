from typing import List

class Solution:
    def findClosedNumbers(self, num: int) -> List[int]:
        MAX_INT, MIN_INT = 2147483648, 0
        if num == 0 or num == MAX_INT:
            return [-1, -1]
        count_1_num = bin(num).count('1')
        big_num = num+1
        small_num = num-1
        while big_num != MAX_INT:
            if bin(big_num).count('1') == count_1_num:
                break
            big_num += 1
        if big_num == MAX_INT:
            big_num = -1
        while small_num != 0:
            if bin(small_num).count('1') == count_1_num:
                break
            small_num -= 1
        if small_num == 0:
            small_num = -1
        return [big_num, small_num]


print(Solution().findClosedNumbers(1))
