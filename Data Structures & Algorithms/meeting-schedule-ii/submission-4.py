class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        res = 0
        count = 0
        e = 0
        for s in range(len(start)):
            if start[s] < end[e]:
                count += 1
            else:
                e += 1
                # count -= 1
            res = max(res, count)
        return res