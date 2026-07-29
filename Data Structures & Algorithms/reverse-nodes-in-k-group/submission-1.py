# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        def getKth(curr, kVal):
            while curr and kVal:
                curr = curr.next
                kVal -= 1
            return curr
        
        dummy = ListNode(0, head)
        groupPrev = dummy
        while True:
            kth = getKth(groupPrev, k)
            if not kth:
                return dummy.next
            
            groupNext = kth.next
            head, prev = groupPrev.next, kth.next
            while head != groupNext:
                next = head.next
                head.next = prev
                prev = head
                head = next
            
            tempNext = groupPrev.next
            groupPrev.next = kth
            groupPrev = tempNext
            
            
        