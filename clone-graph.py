"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node
        stack, seen = [node], {node:Node(node.val, [])}
        while stack:
            cur = stack.pop(0)
            clone = seen[cur]
            for n in cur.neighbors:
                if n not in seen:
                    seen[n] = Node(n.val, [])
                    stack.append(n)
                clone.neighbors.append(seen[n])
        return seen[node]
