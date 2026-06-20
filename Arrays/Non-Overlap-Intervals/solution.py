class Solution:
    def nonOverlapIntervals(intervals):
        intervals.sort(key=lambda interval:interval[1])
        count=0
        prev_end=intervals[0][1]
        for interval in intervals[1:]:
            if interval[0]>=prev_end:
                prev_end=interval[1]
            else:
                count+=1
        return count