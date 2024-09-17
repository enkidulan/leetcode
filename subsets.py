class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return nums
        res = [[]]
        for i, n in enumerate(nums):
            res.append([n])
            for r in self.subsets(nums[i + 1:]):
                res.append([n] + list(r))
        return set([tuple(sorted(i)) for i in res])
