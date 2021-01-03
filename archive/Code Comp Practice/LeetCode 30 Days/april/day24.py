class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.head = None
        self.tail = None
        self.cache = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        # Error - not found
        if key not in self.cache:
            return -1
        # Don't do anything if capacity is 1
        if self.capacity == 1:
            return self.cache[key].val
        # Don't do anything if head
        if self.head.key == key:
            return self.head.val
        # Move tail along if tail
        if self.tail.key == key:
            if self.tail.next:
                self.tail = self.tail.next

        node = self.cache[key]
        # Remove link
        prev = node.prev
        next_ = node.next
        if prev:
            prev.next = next_
        if next_:
            next_.prev = prev
        # Add head
        self.head.next = node
        node.prev = self.head
        self.head = node

        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            # Update by getting the cache value
            self.get(key)
            self.head.val = value
            return

        node = Node(key, value)
        self.cache[key] = node
        if self.head == None:
            self.head = node
            self.tail = node
            return

        node.prev = self.head
        self.head.next = node
        self.head = node
        if len(self.cache) > self.capacity:
            tailKey = self.tail.key
            self.tail = self.tail.next
            self.tail.prev = None
            del self.cache[tailKey]


def pCache():
    print(*[(x.key, x.val) for x in [cache.cache[k] for k in cache.cache]])


cache = LRUCache(2)
pCache()
cache.put(2, 1)
pCache()
cache.put(1, 1)
pCache()
cache.put(2, 3)
pCache()
cache.put(4, 1)
pCache()
print(cache.get(1))
pCache()
print(cache.get(2))
