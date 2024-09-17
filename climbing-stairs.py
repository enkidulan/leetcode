# from functools import lru_cache
# class Solution:
#     @lru_cache(10**10)
#     def climbStairs(self, n: int) -> int:
#         if n in (0, 1, 2, 3):
#             return n
#         return self.climbStairs(n - 1) + self.climbStairs(n - 2)


class Solution:

    def climbStairs(self, n: int) -> int:
        if n in (0, 1):
            return 1
        prev = cur = 1
        for i in range(2, n + 1):
            prev, cur = cur, prev + cur
        return cur
