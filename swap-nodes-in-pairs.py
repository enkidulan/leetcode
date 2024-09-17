# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not getattr(head, "next", None):
            return head
        left, right, root = head, head.next, head.next
        while right:
            tail = right.next
            if tail and tail.next:
                left.next, right.next = tail.next, left
                left, right = tail, tail.next
            else:
                left.next, right.next = tail, left
                right = None
        return root
