# 0---2
# --1-------4
# -------3------5
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])

        ans = [intervals[0]]

        for start, end in intervals:
            lastStart, lastEnd = ans[-1]

            if start <= lastEnd:
                ans[-1][1] = max(lastEnd, end)
            else:
                ans.append([start, end])
        
        return ans
