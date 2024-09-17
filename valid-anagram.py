def count_letters(s):
    count = {}
    for i in s:
        count[i] = count.get(i,0) + 1
    return count

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return count_letters(s) == count_letters(t)

