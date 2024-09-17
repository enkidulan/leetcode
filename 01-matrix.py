import math

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        height, widht = len(mat), len(mat[0])

        for y in range(height):
            for x in range(widht):
                if mat[y][x] > 0:
                    top = mat[y - 1][x] if y > 0 else math.inf
                    left = mat[y][x - 1] if x > 0 else math.inf
                    mat[y][x] = min(top, left) + 1

        for y in range(height - 1, -1, -1):
            for x in range(widht - 1, -1, -1):
                if mat[y][x] > 0:
                    bottom = mat[y + 1][x] if y < height - 1 else math.inf
                    right = mat[y][x + 1] if x < widht - 1 else math.inf
                    mat[y][x] = min(mat[y][x], bottom + 1, right + 1)

        return mat
