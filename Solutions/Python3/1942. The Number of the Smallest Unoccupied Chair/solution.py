class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        target_arrival = times[targetFriend][0]
        times.sort(key=lambda time: time[0])
        
        people = []
        chairs = [i for i in range(len(times))]

        for arrival, leaving in times:
            if arrival > target_arrival:
                continue

            while people and people[0][0] <= arrival:
                _, chair = heappop(people)
                heappush(chairs, chair)
            
            if arrival == target_arrival:
                return chairs[0]

            chair = heappop(chairs)
            heappush(people, (leaving, chair))
