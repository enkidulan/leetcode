mapping = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}

class Solution:
    def romanToInt(self, s: str) -> int:
        total = prev = 0
        for letter  in s:
            val = mapping[letter]
            total = total - prev if val > prev else total + prev
            prev = val
        return total + val

