from typing import List

class Solution:
    def splitIntoFibonacci(self, S: str) -> List[int]:
        ans = list()

        def backtrack(index: int):
            if index == len(S):
                return len(ans) >= 3
            
            curr = 0
            for i in range(index, len(S)):
                if i > index and S[index] == "0":
                    break
                # 组合数值
                curr = curr * 10 + ord(S[i]) - ord("0")
                if curr > 2**31 - 1:
                    break
                
                # 查找符合斐波那契规则的数组，如果符合，则进入递归
                if len(ans) < 2 or curr == ans[-2] + ans[-1]:
                    ans.append(curr)
                    # 递归到下一个索引，查找下一个组合数值
                    if backtrack(i + 1):
                        return True
                    ans.pop()
                # 如果不符合，直接退出，返回FALSE
                elif len(ans) >= 2 and curr > ans[-2] + ans[-1]:
                    break
        
            return False
        
        backtrack(0)
        return ans

print(Solution().splitIntoFibonacci("124"))