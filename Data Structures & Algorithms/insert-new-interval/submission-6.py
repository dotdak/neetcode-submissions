class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # intervals.sort(key=lambda x: x[0])
        if not intervals:
            return [newInterval]
        newStart, newEnd = newInterval
        index = 0
        for k, [start, end] in enumerate(intervals):
            if newStart <= end:
                index = k
                break
        else:
            index = len(intervals)
        if index >= len(intervals) or intervals[index][0] > newEnd:
            intervals.insert(index, newInterval)
        elif intervals[index][1] >= newStart:
            intervals[index][0] = min(intervals[index][0], newStart)
            intervals[index][1] = max(intervals[index][1], newEnd)
        while index + 1 < len(intervals) and intervals[index + 1][0] <= newEnd:
            _, end = intervals.pop(index+1)
            intervals[index][1] = max(end, newEnd)
        return intervals    
        