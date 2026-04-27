# 0---2
# --1-------4
# -------3------5
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        start = sorted([s for [s, e] in intervals])
        end = sorted([e for [s, e] in intervals])

        ans = []
        s = e = 0
        current_start = start[0]
        current_end = end[0]
        count = 0
        while s < len(start):
            if start[s] <= end[e]:
                s += 1
                count += 1
            else:
                current_end = end[e]
                e += 1
                count -= 1
            if count == 0:
                ans.append([current_start, current_end])
                current_start = start[s]
        while e < len(end):
            current_end = max(current_end, end[e])
            e += 1
        ans.append([current_start, current_end])
        return ans