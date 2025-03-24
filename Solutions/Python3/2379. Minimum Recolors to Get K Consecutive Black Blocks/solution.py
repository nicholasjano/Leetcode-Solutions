class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        left = 0
        num_whites = 0
        min_operations = float("inf")

        for right in range(len(blocks)):
            if blocks[right] == "W":
                num_whites += 1

            if right - left + 1 == k:
                min_operations = min(min_operations, num_whites)

                if blocks[left] == "W":
                    num_whites -= 1

                left += 1

        return min_operations