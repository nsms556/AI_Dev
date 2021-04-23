class ArrayQueue :
    def __init__(self) :
        self.data = []
    def size(self) :
        return len(self.data)
    def isEmpty(self) :
        return self.size() == 0
    def enqueue(self, item) :
        self.data.insert(0, item)
    def dequeue(self) :
        return self.data.pop()
    def peek(self) :
        return self.data[-1]

def solution(progresses, speeds):
    answer = []
    a = ArrayQueue()
    
    progresses.reverse()
    speeds.reverse()

    a.data = progresses
    
    while not a.isEmpty() :
        for idx, speed in enumerate(speeds) :
            if a.data[idx] < 100 :
                a.data[idx] += speed
        
        count = 0
        while a.data[-1] >= 100 :
            a.dequeue()
            speeds.pop()
            count += 1
            if a.isEmpty() :
                break
            
        if count != 0 :
            answer.append(count)
                
    return answer