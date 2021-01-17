from typing import List

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        def sort_model(a: list, b: list):
            if a[0] == b[0]:
                return a if a[1]<b[1] else b
            else:
                return a if a[0]>b[0] else b
        envelopes.sort(key=sort_model)
        piles = 0
        n = len(envelopes)
        top = [0]*n
        for i in range(n):
            pocker = envelopes[i]
            left, right = 0, piles
            while left<right:
                mid = (left+right)//2
                if top[mid]>=pocker:
                    right=mid
                else:
                    left = mid+1
            if left==piles: piles += 1
            top[left] = pocker
        return piles

print(Solution().maxEnvelopes([[5,4],[6,4],[6,7],[2,3]]))
