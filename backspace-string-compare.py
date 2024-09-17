def proccess(s):
    stack = []
    for i in s:
        if i == "#":
            if stack:
                stack.pop(-1)
        else:
            stack.append(i)
    return stack

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        return proccess(s) == proccess(t)

