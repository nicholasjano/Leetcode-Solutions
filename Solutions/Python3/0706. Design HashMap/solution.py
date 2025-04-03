class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class MyHashMap:

    def __init__(self):
        self.capacity = 100
        self.size = 0
        self.load_factor_threshold = 0.66
        self.buckets = [None] * self.capacity
        
    def _hash(self, key):
        return key % self.capacity
    
    def _resize(self):
        old_buckets = self.buckets
        self.capacity *= 2
        self.buckets = [None] * self.capacity
        self.size = 0
        
        for bucket in old_buckets:
            current = bucket
            while current:
                self.put(current.key, current.value)
                current = current.next
        
    def put(self, key: int, value: int) -> None:
        index = self._hash(key)
        
        if not self.buckets[index]:
            self.buckets[index] = ListNode(key, value)
            self.size += 1
            if self.size > self.capacity * self.load_factor_threshold:
                self._resize()
            return
            
        current = self.buckets[index]
        while True:
            if current.key == key:
                current.value = value
                return
                
            if not current.next:
                current.next = ListNode(key, value)
                self.size += 1
                if self.size > self.capacity * self.load_factor_threshold:
                    self._resize()
                return
                
            current = current.next
        
    def get(self, key: int) -> int:
        index = self._hash(key)
        current = self.buckets[index]
        
        while current:
            if current.key == key:
                return current.value
            current = current.next
            
        return -1
        
    def remove(self, key: int) -> None:
        index = self._hash(key)
        current = self.buckets[index]
        
        if not current:
            return
            
        if current.key == key:
            self.buckets[index] = current.next
            self.size -= 1
            return
            
        while current.next and current.next.key != key:
            current = current.next
            
        if current.next:
            current.next = current.next.next
            self.size -= 1