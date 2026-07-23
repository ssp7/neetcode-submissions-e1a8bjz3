# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        dummy = ListNode(0, head)

        # extract second half
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None
        # reverse second half
        prev = None
        while second:
            next = second.next
            second.next = prev
            prev = second
            second = next
        
        # prev = head of reversed list
        # 0 1 2
        # 3 4 5
        while prev:
            next, prevNext = head.next, prev.next
            prev.next = next
            head.next = prev
            head, prev = next, prevNext
            
            # head.next = prev
            # prev.next = ext
            # head.next = prev
            # head, prev = next, prevNext



        