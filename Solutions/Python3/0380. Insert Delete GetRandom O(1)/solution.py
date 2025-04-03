class RandomizedSet:

    def __init__(self):
        self.nums = []
        self.pos = defaultdict(int)

    def insert(self, val: int) -> bool:
        if val in self.pos:
            return False
        
        self.pos[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.pos:
            return False
        
        curr_position = self.pos[val]
        final_index = len(self.nums) - 1
        if self.pos[val] != final_index:
            final_value = self.nums[final_index]
            self.nums[curr_position] = final_value
            self.pos[final_value] = curr_position
        
        del self.pos[val]
        self.nums.pop()
        return True

    def getRandom(self) -> int:
        return choice(self.nums)
        

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()