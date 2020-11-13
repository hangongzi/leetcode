class Solution:
    def findSubstring(self, s: str, words: list) -> list:
        if not s or not words:
            return []
        res = []
        from collections import Counter
        all_len = sum(map(lambda x: len(x), words))
        n = len(s)
        word_len = len(words[0])
        words = Counter(words)

        for i in range(n-all_len+1):
            tmp = s[i:all_len]
            c_tmp = []
            for j in range(0, all_len, word_len):
                c_tmp.append(tmp[j:word_len])
            if Counter(c_tmp) == words:
                res.append(i)

        return res


print(Solution().findSubstring("barfoothefoobarman", ["foo", "bar"]))
