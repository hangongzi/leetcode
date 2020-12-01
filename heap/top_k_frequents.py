class Solution(object):
    def topKFrequent(self, nums, k):
        # 堆
        

        # hash_t = {}
        # for n in nums:
        #     if n in hash_t: hash_t[n] += 1
        #     else: hash_t[n] = 1

        # t = sorted(hash_t.items(), key=lambda x: x[1], reverse=True)
        # return list(map(lambda x: x[0], t[:k]))

print(Solution().topKFrequent([1,1,1,2,2,3], 2))