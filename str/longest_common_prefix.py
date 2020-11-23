class Solution:
    def longestCommonPrefix(self, strs: list) -> str:
        if not strs:
            return 
        if len(strs)==1:
            return strs[0]
        def twoCommonPrefix(s1, s2):
            i = 0
            while i<len(s1) and i<len(s2) and s1[i]==s2[i]:
                i += 1
            return s1[:i]
        
        s1 = strs[0]
        for s2 in strs[1:]:
            s1 = twoCommonPrefix(s1, s2)
        return s1 if s1 else ""

print(Solution().longestCommonPrefix(["dog","racecar","car"]))
