
def fill_if_color_match(image, y, x, origin_color, targe_color, visited):
    if (y, x) in visited:
        return
    visited.add((y,x))

    h, w = len(image), len(image[0])
    if not 0 <= y < h:
        return
    if not 0 <= x < w:
        return
    if image[y][x] != origin_color:
        return

    image[y][x] = targe_color

    fill_if_color_match(image, y - 1, x, origin_color, targe_color, visited)
    fill_if_color_match(image, y + 1, x, origin_color, targe_color, visited)
    fill_if_color_match(image, y, x - 1, origin_color, targe_color, visited)
    fill_if_color_match(image, y, x + 1, origin_color, targe_color, visited)


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        origin_color = image[sr][sc]
        fill_if_color_match(image, sr, sc, origin_color, color, set())
        return image
