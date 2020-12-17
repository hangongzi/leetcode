class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        if len(pattern) != len(s):
            return False
        t = {}
        for k, v in zip(pattern, s):
            if k in t:
                if v == t[k]:
                    continue
                else:
                    return False
            if v in t.values():
                return False
            t[k] = v
        return True
            

print(Solution().wordPattern('abba', "dog dog dog dog"))