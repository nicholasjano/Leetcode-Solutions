# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        merged_lists = head
        
        while list1 and list2:
            if list1.val < list2.val:
                merged_lists.next = list1
                list1 = list1.next
            else:
                merged_lists.next = list2
                list2 = list2.next
            merged_lists = merged_lists.next
        
        merged_lists.next = list1 if list1 else list2
        return head.next
