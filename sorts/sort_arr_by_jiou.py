class Solution:
    def sortArrayByParityII(self, A: list) -> list:
        add_num, event_num = [], []
        for i in A:
            if i%2: add_num.append(i)
            else: event_num.append(i)
        ret = []
        for i in zip(add_num, event_num):
            ret.append(i[1])
            ret.append(i[0])

        return ret


print(Solution().sortArrayByParityII([4, 2, 5, 7]))