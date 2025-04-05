# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr
    
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        prevGroup = dummy
        while True:
            kth = self.getKth(prevGroup, k)
            if not kth:
                return dummy.next
            
            nextGroup = kth.next

            prev, curr = nextGroup, prevGroup.next
            while curr != nextGroup:
                third = curr.next
                curr.next = prev
                prev, curr = curr, third
            
            newEnd = prevGroup.next
            prevGroup.next = kth
            prevGroup = newEnd
            
