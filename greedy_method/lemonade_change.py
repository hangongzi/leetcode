from typing import List

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        l = {5:0, 10:0, 20:0}
        for i in bills:
            if i == 5:
                l[5] += 1
            elif i == 10:
                l[10] += 1
                if l[5]:
                    l[5] -= 1
                else: return False
            elif i == 20:
                l[20] += 1
                if l[10]>0 and l[5]>0:
                    l[10] -= 1
                    l[5] -= 1
                elif l[5]>=3:
                    l[5] -= 3
                else:
                    return False

        return True

print(Solution().lemonadeChange([5,5,10,10,20]))


    