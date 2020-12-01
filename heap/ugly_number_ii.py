from heapq import heappop, heappush

class Ugly:
    def __init__(self):
        self.nums = nums = []
        seen = {1, }
        heap = []
        heappush(heap, 1)

        for _ in range(1690):
            curr_ugly = heappop(heap)
            self.nums.append(curr_ugly)
            for i in [2, 3, 5]:
                new_ugly = curr_ugly*i
                if new_ugly not in seen:
                    seen.add(new_ugly)
                    heappush(heap, new_ugly)


class Ugly1:
    def __init__(self):
        self.nums = nums = [1, ]
        i2 = i3 = i5 = 0
        for i in range(1, 1690):
            ugly = min(nums[i2]*2, nums[i3]*3, nums[i5]*5)
            nums.append(ugly)
            if ugly == nums[i2]*2:
                i2 += 1
            if ugly == nums[i3]*3:
                i3 += 1
            if ugly == nums[i5]*5:
                i5 += 1


class Solution(object):
    u = Ugly1()
    def nthUglyNumber(self, n):
        return self.u.nums[n-1]

print(Solution().nthUglyNumber(10))
