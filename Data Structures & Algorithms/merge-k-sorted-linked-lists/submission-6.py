# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        while len(lists) > 1:
            finalList = []
            for i in range(0, len(lists), 2): # keep splitting them into halfs
                l1 = lists[i] # first
                l2 = lists[i + 1] if (i + 1) < len(lists) else None # second
                finalList.append(self.merge2Lists(l1, l2)) # append the merged list of l1 and l2
            
            lists = finalList #
        return lists[0]

        
    def merge2Lists(self, l1, l2):
        dummy = ListNode(0, self)
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        
        if l1 != None:
            tail.next = l1
        if l2 != None:
            tail.next = l2
        return dummy.next






