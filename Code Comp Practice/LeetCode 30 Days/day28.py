class Node:
    def __init__(self, val):
        self.next = None
        self.prev = None
        self.val = val


class FirstUnique:

    def __init__(self, nums):
        self.d = {}
        self.head = None
        self.tail = None
        for n in nums:
            self.add(n)

    def showFirstUnique(self):
        return -1 if self.tail == None else self.tail.val

    def add(self, val):
        if val in self.d:
            if self.d[val] != None:
                node = self.d[val]
                # Remove link
                if node == self.head:
                    self.head = node.prev
                if node == self.tail:
                    self.tail = node.next
                prev = node.prev
                next_ = node.next
                if prev:
                    prev.next = next_
                if next_:
                    next_.prev = prev
                del self.d[val]
                self.d[val] = None
        else:
            node = Node(val)
            if self.head == None:
                self.head = node
                self.tail = node
            else:
                self.head.next = node
                node.prev = self.head
                self.head = node
            self.d[val] = node

sol = FirstUnique([2,3,5])
print(sol.showFirstUnique())
sol.add(5)
print(sol.showFirstUnique())
sol.add(2)
print(sol.showFirstUnique())
sol.add(3)
print(sol.showFirstUnique())
sol.add(3)
print(sol.showFirstUnique())
sol.add(1)
print(sol.showFirstUnique())
