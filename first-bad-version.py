# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        lower, upper = 0, n
        for i in range(n):
            middle = (lower + upper) //  2
            if isBadVersion(middle):
                upper = middle
            else:
                lower = middle
            if upper - 1 <= lower:
                return upper
        raise RuntimeError("Didn't bad version find in the expected number of steps")
