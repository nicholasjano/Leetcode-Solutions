class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        plantGrowPairs = list(zip(plantTime, growTime))
        plantGrowPairs.sort(key=lambda pair: pair[1])

        cumulativeDays, minDays = 0, 0
        while plantGrowPairs:
            currentPlantTime, currentGrowTime = plantGrowPairs.pop()
            cumulativeDays += currentPlantTime
            minDays = max(minDays, cumulativeDays + currentGrowTime)
        
        return minDays