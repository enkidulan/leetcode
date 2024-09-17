class Solution:
    def search(self, nums: List[int], target: int) -> int
        lower = 0
        upper = len(nums) - 1
        for _ in nums:
            index = (upper + lower) // 2
            if nums[index] == target:
                return index
            if upper == lower:
                return -1
            if nums[index] > target:
                upper = index - 1
            elif nums[index] < target:
                lower = index + 1
        return -1
