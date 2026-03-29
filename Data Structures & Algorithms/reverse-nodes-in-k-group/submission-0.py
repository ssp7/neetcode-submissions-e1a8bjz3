# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        dummy = ListNode(0, head)
        groupPrev = dummy

        def getKth(node, kVal):
            while node and kVal:
                node = node.next
                kVal -= 1
            return node
        
        while True:
            kth = getKth(groupPrev, k)
            if not kth:
                return dummy.next
            
            groupNext = kth.next
            prev, curr = groupNext, groupPrev.next
            while curr != groupNext:
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next
            
            temp = groupPrev.next
            groupPrev.next = kth
            groupPrev = temp









