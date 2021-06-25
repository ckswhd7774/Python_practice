# 선형큐
class Queue :
    
    def __init__(self, Qsize) :
        self.front = 0
        self.rear = 0
        self.capacity = Qsize
        self.List = [None] * self.capacity
        
    def isEmpty(self) :
        flag = False
        if self.front == self.rear :
            flag = True
        return flag
    
    def append(self, value) :
        self.List[self.rear] = value
        self.rear += 1
    
    def popleft(self) :
        if not self.isEmpty() :
            answer = self.List[self.front]
            self.List[self.front] = None
            self.front += 1
            return answer
        else :
            return None
    def show(self) :
        out = []
        out = self.List[self.front:self.rear]
        return out
    
Q = Queue(5)
Q.append(3)
Q.append(5)
Q.append(7)
Q.show()
print(Q.popleft())
Q.show()