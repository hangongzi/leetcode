class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        if not s and not t:
            return True

        tmp = {}
        for i in range(len(s)):
            if s[i] not in tmp:
                if t[i] in tmp.values():
                    return False
                else:
                    tmp[s[i]] = t[i]
            else:
                if tmp[s[i]] != t[i]:
                    return False

        return True

print(Solution().isIsomorphic('add', 'egd'))
