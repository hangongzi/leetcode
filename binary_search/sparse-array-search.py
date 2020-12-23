from typing import List


class Solution:
    def findString(self, words: List[str], s: str) -> int:
        n = len(words)
        low, up = 0, n-1
        
        while low <= up:
            mid_bak = mid = (low+up)//2
            while mid<=up and words[mid] == "":
                mid += 1
            if mid>up:
                up = mid_bak-1
                continue

            if words[mid]>s:
                up = mid-1
            elif words[mid]<s:
                low = mid+1
            else:
                return mid
        return -1


print(Solution().findString(
    ["at", "", "", "", "ball", "", "", "car", "", "","dad", "", ""], 
    "ta"))

