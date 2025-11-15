class MyCircularQueue:

    def __init__(self, k: int):
        self.circle = [None] * k
        self.head, self.rear = 0,0 
        self.max_len = k

    def enQueue(self, value: int) -> bool:
        if self.circle[self.rear] == None:
            self.circle[self.rear] = value 
            self.rear = (self.rear+1) % self.max_len
            return True
        else:
            return False 
    def deQueue(self) -> bool:
        if self.circle[self.head] == None:
            return False
        else:
            self.circle[self.head] = None
            self.head = (self.head + 1 )%self.max_len
            return True 

    def Front(self) -> int:
        return -1 if self.circle[self.head] is None else self.circle[self.head]

    def Rear(self) -> int:
        return -1 if self.circle[self.rear-1] is None else self.circle[self.rear-1]

    def isEmpty(self) -> bool:
        return self.head == self.rear and self.circle[self.head] is None 

    def isFull(self) -> bool:
        return self.rear == self.head and self.circle[self.head] is not None 


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()