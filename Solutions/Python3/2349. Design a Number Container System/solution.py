class NumberContainers:
    def __init__(self):
        self.index_to_number = {}
        self.number_to_indices = {}
        self.valid_indices = {}

    def change(self, index: int, number: int) -> None:
        if index in self.index_to_number and self.index_to_number[index] == number:
            return

        if index in self.index_to_number:
            old_number = self.index_to_number[index]
            if old_number in self.valid_indices:
                self.valid_indices[old_number].discard(index)
        
        self.index_to_number[index] = number
        
        if number not in self.number_to_indices:
            self.number_to_indices[number] = []
            self.valid_indices[number] = set()

        heappush(self.number_to_indices[number], index)
        self.valid_indices[number].add(index)

    def find(self, number: int) -> int:
        if number not in self.number_to_indices or not self.valid_indices[number]:
            return -1

        while self.number_to_indices[number] and self.number_to_indices[number][0] not in self.valid_indices[number]:
            heappop(self.number_to_indices[number])

        return self.number_to_indices[number][0] if self.number_to_indices[number] else -1
        