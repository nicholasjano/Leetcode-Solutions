# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        prev = head

        # Used for max
        lowest_cp = -1
        highest_cp = -1
        # Used for min
        lowest_range = -1
        last_critical = -1

        current = head.next
        current_pos = 1
        while current.next:
            if (current.val < prev.val and current.val < current.next.val) \
            or (current.val > prev.val and current.val > current.next.val):
                if lowest_cp == -1:
                    lowest_cp = current_pos
                else:
                    highest_cp = current_pos
                
                if last_critical != -1:
                    if lowest_range == -1:
                        lowest_range = current_pos - last_critical
                    else:
                        lowest_range = min(lowest_range, current_pos - last_critical)
                last_critical = current_pos
            
            prev = current
            current = current.next
            current_pos += 1
        
        if lowest_cp == -1 or highest_cp == -1 or lowest_range == -1:
            return [-1, -1]
        
        return [lowest_range, highest_cp - lowest_cp]