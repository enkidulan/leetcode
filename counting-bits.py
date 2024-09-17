"""
0000
0001
0010
0011

0100
0101
0110
0111

1000
1001
1010
1011
1100
1101
1111


"""


class Solution:
    def countBits(self, n: int) -> List[int]:
        t = [0 for i in range(n + 1)]
        for i in range(n + 1):
            t[i] = t[i >> 1] + i % 2
        return t
