class CircularQueue:
    def __init__(self, n):
        self.maxCount = n
        self.data = [None] * n
        self.count = 0
        self.front = -1
        self.rear = -1

    def size(self):
        return self.count

    def isEmpty(self):
        return self.count == 0

    def isFull(self):
        return self.count == self.maxCount

    def enqueue(self, x):
        if self.isFull():
            raise IndexError('Queue full')
            
        self.rear = (self.rear + 1) % self.maxCount

        self.data[self.rear] = x
        self.count += 1

    def dequeue(self):
        if self.isEmpty() : 
            raise IndexError('Queue empty')
        
        self.front = (self.front + 1) % self.maxCount

        x = self.data[self.front]

        self.count -= 1
        return x

    def peek(self):
        if self.isEmpty():
            raise IndexError('Queue empty')
        return self.data[(self.front + 1) % self.maxCount]

def solution(x):
    return 0

b = CircularQueue(6)

b.enqueue(1)
b.enqueue(12)
b.enqueue(432)
b.enqueue(23)
b.enqueue(9)

print(b.data, b.front, b.rear)
print(b.dequeue())
print(b.data, b.front, b.rear)
b.enqueue(5)
print(b.data, b.front, b.rear)
print(b.peek())
b.enqueue(7)
print(b.isFull())
print(b.data, b.front, b.rear)
print(b.dequeue())
print(b.data, b.front, b.rear)
print(b.dequeue())
print(b.dequeue())
print(b.dequeue())
print(b.dequeue())
print(b.data, b.front, b.rear)
print(b.peek())
print(b.dequeue())
print(b.data, b.front, b.rear)
print(b.isEmpty())