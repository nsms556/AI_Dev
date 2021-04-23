class MaxHeap:
    def __init__(self):
        self.data = [None]

    def insert(self, item):
        key = len(self.data)
        self.data.append(item)

        while key != 1 and key > 1 and self.data[key//2] < self.data[key] :
            self.data[key//2], self.data[key] = self.data[key], self.data[key//2]
            key = key // 2

a = MaxHeap()

a.insert(3)
a.insert(1)
print(a.data)
a.insert(2)

print(a.data)
a.insert(5)
print(a.data)