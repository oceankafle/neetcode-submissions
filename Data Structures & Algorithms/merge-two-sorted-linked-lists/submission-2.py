# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy      # start the list off with a dummy node

        while l1 and l2: # are not null
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next  # update that dummy node after all comparisons to be the original first one
        if l1:   # if l1 is not null
            tail.next = l1
        elif l2: # if l2 is not null
            tail.next = l2

        return dummy.next
         

