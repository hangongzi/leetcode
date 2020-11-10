class Solution:
    def insert(self, intervals: list, newInterval: list) -> list:
        ret = []
        placed = False
        left, right = newInterval
        for interval in intervals:
            if interval[0] > right:
                if not placed:
                    ret.append([left, right])
                    placed = True
                ret.append(interval)
            elif interval[1] < left:
                ret.append(interval)
            else:
                left = min(left, interval[0])
                right = max(right, interval[1])
        if not placed:
            ret.append([left, right])

        return ret


print(Solution().insert([[1,5],[6,8]], [4,9]))
