class LFUCache:
    # cnt(x) = the use counter for key x
    # cache=[] will show the last used order for tiebreakers 
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.frequencies = defaultdict(OrderedDict)
        self.lfu_min = 1

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        value, frequency = self.cache[key]
        del self.frequencies[frequency][key]
        self.frequencies[frequency + 1][key] = True
        self.cache[key] = (value, frequency + 1)

        if (
            (frequency == self.lfu_min) and 
            (len(self.frequencies[frequency]) == 0)
        ):
            self.lfu_min += 1

        return value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            _, frequency = self.cache[key]
            del self.frequencies[frequency][key]
            self.frequencies[frequency + 1][key] = True
            self.cache[key] = (value, frequency + 1)
            if (
                (frequency == self.lfu_min) and 
                (len(self.frequencies[frequency]) == 0)
            ):
                self.lfu_min += 1
        else:
            if len(self.cache) + 1 > self.capacity:
                del_key, _ = self.frequencies[self.lfu_min].popitem(last=False)
                del self.cache[del_key]

            self.cache[key] = (value, 1)
            self.frequencies[1][key] = True
            self.lfu_min = 1
        

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)