# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode], level=0, result=None) -> List[List[int]]:
        if result is None:
            result = {}
        if not root:
            return []
        result.setdefault(level, []).append(root.val)
        self.levelOrder(root.left, level+1, result)
        self.levelOrder(root.right, level+1, result)
        if level == 0:
            return list(result.values())
