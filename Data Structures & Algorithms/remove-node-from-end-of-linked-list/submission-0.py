# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        idx = 0
        dummy = ListNode(0, head)
        left, right = dummy, head

        while idx < n:
            right = right.next
            idx += 1
        
        while right:
            left = left.next
            right = right.next
        
        left.next = left.next.next
        
        return dummy.next
        
            