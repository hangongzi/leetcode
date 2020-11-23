from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: list) -> list:
        if not words or not s:
            return []
        sub_len = len(words[0])*len(words)
        word_len = len(words[0])
        words_cnt = Counter(words)
        ans = []
        for i in range(0,len(s)-sub_len+1):
            sub_s = s[i:i+sub_len]
            tmp = Counter([sub_s[i*word_len: (i+1)*word_len] for i in range(len(words))])
            if words_cnt == tmp:
                ans.append(i)

        return ans
        # if not s or not words:
        #     return []
        # res = []
        # from collections import Counter
        # all_len = sum(map(lambda x: len(x), words))
        # n = len(s)
        # word_len = len(words[0])
        # words = Counter(words)

        # for i in range(n-all_len+1):
        #     tmp = s[i:i+all_len]
        #     c_tmp = []
        #     for j in range(0, all_len, word_len):
        #         c_tmp.append(tmp[j:j+word_len])
        #     if Counter(c_tmp) == words:
        #         res.append(i)

        # return res


print(Solution().findSubstring("lingmindraboofooowingdingbarrwingmonkeypoundcake", ["fooo","barr","wing","ding","wing"]))
