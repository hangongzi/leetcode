from typing import List


class Solution:
    def longestWord(self, words: List[str]) -> str:
        def isCombanded(set_words: set, word: str)->bool:
            if not word:
                return True
            # 回溯法
            for i in range(len(set_words)):
                if set_words[i] in word and isCombanded(set_words, word.replace(set_words[i], '')):
                    return True
            return False

        words.sort(key=lambda x: -len(x))
        ans = []
        for i in range(len(words)):
            if ans and len(ans[-1])>len(words[i]):
                break
            if isCombanded(words[i+1:], words[i]):
                ans.append(words[i])
        if not ans:
            return ""
        ans.sort()
        return ans[0]

print(Solution().longestWord(["bbbbb","bbbbbb","bb","bb","bbb","bbbbb","bbbbbbbb","bbb","bbbbbbb"]))
