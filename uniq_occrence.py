class Solution:
    def uniqueOccurrences(self, arr: list) -> bool:
        num_dict = {}
        for i in arr:
            if i in num_dict:
                num_dict[i] += 1
            else:
                num_dict[i] = 1
        return len(list(set(num_dict.values())))==len(list(num_dict.keys()))

print(Solution().uniqueOccurrences([1,1,2,2,2,3]))
