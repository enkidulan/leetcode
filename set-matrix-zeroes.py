class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        changed = set()
        for y in range(len(matrix)):
            for x in range(len(matrix[y])):
                if matrix[y][x] != 0:
                    continue
                if (y, x) in changed:
                    continue
                for y1 in range(len(matrix)):
                    if matrix[y1][x] != 0:
                        changed.add((y1,x))
                    matrix[y1][x] = 0
                for x1 in range(len(matrix[y])):
                    if matrix[y][x1] != 0:
                        changed.add((y,x1))
                    matrix[y][x1] = 0
