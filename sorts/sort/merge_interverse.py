class Solution:
    def merge(self, intervals):
        intervals.sort(key=lambda x: x[0])
        result = list()
        for interval in intervals:
            if not result or result[-1][1]<interval[0]:
                result.append(interval)
            else:
                result[-1][1] = max(result[-1][1], interval[1])
        return result

intervals = [[2,3],[4,5],[6,7],[8,9],[1,10]]

Solution().merge(intervals)
