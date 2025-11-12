class MyCircularQueue:

    def __init__(self, k: int):
        self.circle = [None] * k 
        self.max_len = k 
        self.first = 0 
        self.rear = 0  

    def enQueue(self, value: int) -> bool:
        if self.circle[self.rear] is None:
            self.circle[self.rear] = value 
            # 이동 
            self.rear = (self.rear + 1) % self.max_len
            return True 
        else:
            return False 
    def deQueue(self) -> bool:
        if self.circle[self.first] is not None:
            self.circle[self.first] = None 
            self.first = (self.first + 1) % self.max_len
            return True 
        else:
            return False

    def Front(self) -> int:
        return -1 if self.circle[self.first] is None else self.circle[self.first]

    def Rear(self) -> int:
        return -1 if self.circle[self.rear-1] is None else self.circle[self.rear-1]

    def isEmpty(self) -> bool:
        return self.first == self.rear and self.circle[self.first] is None 

    def isFull(self) -> bool:
        return self.first == self.rear and self.circle[self.first] is not None 
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()