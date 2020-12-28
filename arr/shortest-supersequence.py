from typing import List

class Solution:
    def shortestSeq(self, big: List[int], small: List[int]) -> List[int]:
        import collections
        cnt = collections.Counter(small)
        l = 0
        n = 0
        ans = []
        for r,ch in enumerate(big):
            if ch not in cnt:   #不在cnt 继续
                continue
            cnt[ch] -= 1         #在cnt
            if cnt[ch] == 0:
                n += 1          #统计n
            while big[l] not in cnt or cnt[big[l]] < 0: #移动左指针：big[l]不在cnt，或者big[l]出现不止一次
                if cnt[big[l]] < 0:
                    cnt[big[l]] += 1    #如果出现不止一次， 左指针右移，并加一
                l += 1
            if n == len(cnt):          #如果符合题目条件：
                if not ans or (ans[1]-ans[0]) > r - l:   #找最小串
                    ans = []
                    ans.append(l)
                    ans.append(r)
        return ans

big = [1,2,6,5,3,2,4,1]
small = [1,2,3]
print(Solution().shortestSeq(big, small))
