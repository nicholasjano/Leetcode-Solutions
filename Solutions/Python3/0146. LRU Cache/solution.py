class ListNode:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.head = ListNode(-1, -1)
        self.tail = ListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.add(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            replacement_node = self.cache[key]
            self.remove(replacement_node)
        
        node = ListNode(key, value)
        self.cache[key] = node
        self.add(node)
        if len(self.cache) > self.capacity:
            removal_node = self.head.next
            del self.cache[removal_node.key]
            self.remove(removal_node)
    
    def add(self, node):
        previous_recent = self.tail.prev
        previous_recent.next = node
        node.prev = previous_recent
        node.next = self.tail
        self.tail.prev = node
    
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)