class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        out = []
        s,e = newInterval
        i, n = 0, len(intervals)

        while i < n and s > intervals[i][0]:
            out.append(intervals[i])
            i += 1

        if not out or out[-1][1] < s:
            out.append(newInterval)
        else:
            out[-1][1] = max(out[-1][1], e)

        while i < n:
            interval = intervals[i]
            if out[-1][1] < interval[0]:
                out.append(interval)
            else:
                out[-1][1] = max(out[-1][1], interval[1])
            i+=1

        return out
