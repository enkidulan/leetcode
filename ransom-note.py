def count(s):
    count = {}
    for i in s:
        count[i] = count.get(i, 0) + 1
    return count

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNote_count = count(ransomNote)
        magazine_count = count(magazine)
        for k, c in ransomNote_count.items():
            if magazine_count.get(k, 0) < c:
                return False
        return True

