import itertools

class Solution:
    def letterCombinations(self, digits: str)->list:
        if not digits:
            return []
        phoneMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        groups = [phoneMap[i] for i in digits]
        return [''.join(i) for i in itertools.product(phoneMap[i] for i in digits)]

        # def backtrace(idx):
        #     if idx == len(digits):
        #         combinations.append(''.join(combination))
        #     else:
        #         digit = digits[idx]
        #         for c in phoneMap[digit]:
        #             combination.append(c)
        #             backtrace(idx+1) # 前进匹配
        #             combination.pop() # 回退

        # combination = []
        # combinations = []

        # backtrace(0)
        # return combinations

print(Solution().letterCombinations('23'))