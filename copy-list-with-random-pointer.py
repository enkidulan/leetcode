"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        stack = [head]
        root = Node(head.val)
        node_index = {head: root}
        while stack:
            node = stack.pop(0)
            node_copy = node_index[node]
            node_copy.random = node.random
            if node.next:
                next_node_copy = Node(node.next.val)
                stack.append(node.next)
                node_copy.next = next_node_copy
                node_index[node.next] = next_node_copy

        node = root
        while node:
            if node.random is not None:
                copy_node = node_index[node.random]
                node.random = copy_node
            node = node.next

        return root
