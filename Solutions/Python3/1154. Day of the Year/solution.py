class Solution:
    def dayOfYear(self, date: str) -> int:
        year = int(date[:4])

        month = -1
        if date[5] == 0:
            month = int(date[6])
        else:
            month = int(date[5] + date[6])
        
        day = -1
        if date[8] == 0:
            day = int(date[9])
        else:
            day = int(date[8] + date[9])

        days_in_all_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            days_in_all_months[1] += 1
        
        return sum(days_in_all_months[:month-1]) + day
