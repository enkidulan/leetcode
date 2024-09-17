# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def depth(node, state):
    if not node:
        return 0
    left_d = depth(node.left, state)
    right_d = depth(node.right, state)
    state['max_d']  = max(state['max_d'], right_d + left_d)
    return 1 + max(left_d, right_d)

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        state = {"max_d": 0}
        depth(root, state)
        return state["max_d"]
