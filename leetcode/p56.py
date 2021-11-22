from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_intervals = sorted(intervals, key=lambda x: x[0])
        result = [sorted_intervals[0]]
        for interval in sorted_intervals[1:]:
            low, high = interval

            r_low, r_high = result[-1]
            if r_low <= low <= r_high:
                if high > r_high:
                    r_high = high
                    result[-1][1] = r_high
            else:
                result.append([low, high])

        return result

print(Solution().merge([[1,3],[2,6],[8,10],[15,18]]))
print(Solution().merge([[1,4],[4,5]]))
print(Solution().merge([[1,4],[1,4]]))
