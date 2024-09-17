class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = left = 0
        seen = set()
        for right, l in enumerate(s):
            while l in seen:
                seen.remove(s[left])
                left +=1
            seen.add(l)
            current_len = right - left + 1
            max_len = max(current_len, max_len)
        return max_len
