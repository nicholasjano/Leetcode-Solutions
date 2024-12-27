class Solution:
    def bestIndex(self, num_i, i, num_j, j):
        sum_i = num_i + i
        sum_j = num_j + j

        if sum_j >= sum_i:
            return j
        
        return i

    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        i = 0
        highest_value = float("-inf")
        for j in range(1, len(values)):
            value = values[i] + values[j] + i - j

            i = self.bestIndex(values[i], i, values[j], j)
            highest_value = max(highest_value, value)

        return highest_value