class Solution:
    def combine(self, n: int, k: int, i=1) -> List[List[int]]:
        res = []
        if k == 1:
            return [[p] for p in range(i, n+1)]
        for j in range(i, n + 1):
            for r in self.combine(n, k=k-1, i=j+1):
                res.append([j] + r)
        return res
