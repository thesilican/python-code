class Node:
    def __init__(self, val: int):
        self.val = val
        self.next = None
        self.isMin = False

class MinStack:

    def __init__(self):
        self.head = None
        self.minHead = None

    def push(self, x: int) -> None:
        # Stacc
        n = Node(x)
        n.next = self.head
        self.head = n
        # Min Stacc
        if self.minHead == None or x < self.minHead.val:
            n.isMin = True
            
            m = Node(x)
            m.next = self.minHead
            self.minHead = m

    def pop(self) -> None:
        n = self.head
        self.head = self.head.next
        if n.isMin:
            self.minHead = self.minHead.next

    def top(self) -> int:
        return self.head.val

    def getMin(self) -> int:
        return self.minHead.val


if __name__ == "__main__":
    stacc = MinStack()
    stacc.push(-2)
    stacc.push(0)
    stacc.push(-3)
    print(stacc.getMin())
    stacc.pop()
    print(stacc.top())
    print(stacc.getMin())