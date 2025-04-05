class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        prefix_sums = [None] * n
        prefix_sum = 0
        for i, char in enumerate(s):
            if char == "*":
                prefix_sum += 1
            prefix_sums[i] = prefix_sum

        # Closest candle to the right of each index
        closest_candle_to_right = [None] * n
        most_recent_candle_right = None
        for i in range(len(s) - 1, -1, -1):
            char = s[i]
            if char == "|":
                most_recent_candle_right = i
            closest_candle_to_right[i] = most_recent_candle_right

        # Closest candle to the left of each index
        closest_candle_to_left = [None] * n
        most_recent_candle_left = None
        for i, char in enumerate(s):
            if char == "|":
                most_recent_candle_left = i
            closest_candle_to_left[i] = most_recent_candle_left
        
        answer = []
        for left, right in queries:
            leftmost_candle = closest_candle_to_right[left]
            rightmost_candle = closest_candle_to_left[right]

            if (
                (leftmost_candle is None) or
                (rightmost_candle is None) or
                (leftmost_candle >= rightmost_candle)
            ):
                answer.append(0)
            else:
                answer.append(prefix_sums[rightmost_candle] - prefix_sums[leftmost_candle])
        
        return answer