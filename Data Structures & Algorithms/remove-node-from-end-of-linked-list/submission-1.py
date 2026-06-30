# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head) # init dummy with value 0 and next pointer to the head
        left = dummy # start the left pointer at the dummy node
        right = head # start right off at the head, well move it by n steps in the next step

        for _ in range(n):
            right = right.next
        
        while right:
            left = left.next
            right = right.next
        
        # means right is at the end 
        left.next = left.next.next
        return dummy.next



        
