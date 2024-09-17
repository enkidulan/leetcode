class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        nums = iter(nums)
        max_sum = window_sum = next(nums)
        for n in nums:
            window_sum = n if window_sum + n < n else window_sum + n
            max_sum = max(window_sum, max_sum)
        return max_sum
