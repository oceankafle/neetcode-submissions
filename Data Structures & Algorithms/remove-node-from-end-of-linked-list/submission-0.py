# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head

        while n > 0 and right: # isnt' null
            right = right.next
            n -= 1
        
        while right:
            left = left.next
            right = right.next
        
        # means right is at the end 
        left.next = left.next.next
        return dummy.next

        # dummy-->1-->2-->3-->4-->5-->Null   where n = 2
        #                 l            r --> when right.next hits null: we set left.next to where the right pointer is
        #  curr-->1-->2-->3-->4-->Null
        #
        # return dummy.next since that's the head


        
