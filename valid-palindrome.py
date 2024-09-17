import string

alphanumeric = set(string.ascii_lowercase + string.digits)

class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = [i for i in s.lower() if i in alphanumeric]
        return  cleaned == cleaned[::-1]
