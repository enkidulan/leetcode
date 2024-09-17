# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def count_depth(node):
    # -1 is a marker that singnal unbalanced three
    if not node:
        return 0
    left_depth, right_depth = count_depth(node.left), count_depth(node.right)
    if -1 in (left_depth, right_depth) or  abs(left_depth - right_depth) > 1:
        return -1
    return 1 + max(left_depth, right_depth)

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return count_depth(root) >= 0
