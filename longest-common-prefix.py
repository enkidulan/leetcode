class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common = []
        if len(strs) == 1:
            return strs[0]
        for i, c in enumerate(strs[0]):
            try:
                if set(l[i] for l in strs[1:]) == {c}:
                    common.append(c)
                else:
                    break
            except IndexError:
                break
        return "".join(common)
