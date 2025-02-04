class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        if groupSize == 1:
            return True
        
        card_counts = Counter(hand)
        heap = list(card_counts.keys())
        heapify(heap)

        while heap:
            start = heap[0]
            for i in range(start, start + groupSize):
                if card_counts.get(i, 0) == 0:
                    return False
                card_counts[i] -= 1
                if card_counts[i] == 0:
                    if i != heap[0]:
                        return False
                    heapq.heappop(heap)

        return True
