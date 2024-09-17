class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = r = 0
        while l < len(nums):
            while r < len(nums):
                if nums[r] < nums[l]:
                    pos = 0 if nums[r] == 0 else l
                    nums.insert(pos, nums.pop(r))
                    l += 1
                r += 1
            l += 1
            r = l + 1
