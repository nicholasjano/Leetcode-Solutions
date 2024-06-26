# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry_over = 0
        current = ListNode()
        head = current

        while l1 or l2:
            if l1:
                current.val += l1.val
            if l2:
                current.val += l2.val

            carry_over = current.val // 10
            current.val -= 10 * carry_over
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            if l1 or l2 or carry_over > 0:
                current.next = ListNode()
                current = current.next
                current.val = carry_over

        return head
