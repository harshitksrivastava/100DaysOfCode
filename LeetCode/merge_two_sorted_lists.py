# Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the
# nodes of the first two lists.


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        temphead = ListNode(0)
        curr = temphead
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                curr.next = l1
                curr = curr.next
                l1 = l1.next
            else:
                curr.next = l2
                curr = curr.next
                l2 = l2.next
        if l1 is not None:
            curr.next = l1
        if l2 is not None:
            curr.next = l2
        return temphead.next


