# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:   
        if not lists:
            return None
        
        k = len(lists)
        interval = 1
        while interval < k:
            for i in range(0, k - interval, interval * 2):
                lists[i] = self.mergeLists(lists[i], lists[i + interval])
            interval *= 2
        
        return lists[0]
    
    def mergeLists(self, list1, list2):
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
