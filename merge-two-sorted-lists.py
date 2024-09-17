# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


def rebind(list1, list2):
        l1v = getattr(list1, "val", float("inf"))
        l2v = getattr(list2, "val", float("inf"))
        if l1v < l2v:
            node = list1
            list1 = list1 and list1.next
        else:
            node = list2
            list2 = list2 and list2.next
        return node, list1, list2

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        root, list1, list2 = rebind(list1, list2)
        current = root
        while list1 and list2:
            node, list1, list2 = rebind(list1, list2)
            current.next, current = node, node
        if current:
            current.next = list1 or list2
        return root
