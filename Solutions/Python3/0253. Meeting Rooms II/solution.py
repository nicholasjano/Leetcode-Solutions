class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        n = len(intervals)
        start_values = sorted([start_interval for start_interval, end_interval in intervals])
        end_values = sorted([end_interval for start_interval, end_interval in intervals])
        rooms = 0
        max_rooms = 0
        start_pointer = 0
        end_pointer = 0
        while start_pointer < n:
            start_value = start_values[start_pointer]
            end_value = end_values[end_pointer]
            
            if start_value < end_value:
                rooms += 1
                max_rooms = max(max_rooms, rooms)
                start_pointer += 1
            else:
                rooms -= 1
                end_pointer += 1

        return max_rooms
                