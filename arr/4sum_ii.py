class Solution(object):
    def fourSumCount(self, A, B, C, D):
        hash_table = {}
        for i in A:
            for j in B:
                if i+j not in hash_table: hash_table[i+j] = 1
                else: hash_table[i+j] += 1

        ans = 0
        for k in C:
            for l in D:
                if hash_table.get(-(k+l)):
                    ans += hash_table[-(k+l)]

        return ans

print(Solution().fourSumCount([-1,-1],[-1,1],[-1,1],[1,-1]))
