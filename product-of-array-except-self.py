from itertools import accumulate
from operator import mul

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_2_right = list(accumulate(nums, mul))
        nums.reverse()
        right_2_left = list(accumulate(nums, mul))
        right_2_left.reverse()
        result = [right_2_left[1]]
        for i in range(1, len(nums) - 1):
            result.append(left_2_right[i-1] * right_2_left[i+1])
        result.append(left_2_right[-2])
        return result





