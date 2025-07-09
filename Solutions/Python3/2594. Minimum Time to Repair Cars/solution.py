class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        cars_squared = cars * cars
        left = 1
        right = ranks[0] * cars_squared 
        min_time = right
        while left <= right:
            time = (left + right) // 2

            total_cars = 0
            for rank in ranks:
                total_cars += floor(sqrt(time/rank))
            
            if total_cars >= cars:
                min_time = time
                right = time - 1
            else:
                left = time + 1
        
        return min_time
