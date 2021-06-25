# 원형큐
class Queue :
    
    def __init__(self, Qsize) :
        self.front = 0
        self.rear = 0
        self.capacity = Qsize
        self.List = [None] * self.capacity
        
    def isEmpty(self) :
        flag = False
        if self.front == self.rear and self.List[self.front] == None :
            flag = True
        return flag
    
    def isFull(self) :
        flag = False
        if self.front == self.rear and self.List[self.front] != None :
            flag = True
        return flag
    
    def append(self, value) :
        if not self.isFull() :
            self.List[self.rear] = value
            self.rear = (self.rear + 1) % self.capacity
            return True
        else :
            return False
    
    def popleft(self) :
        if not self.isEmpty() :
            answer = self.List[self.front]
            self.List[self.front] = None
            self.front = (self.front + 1) % self.capacity
            return answer
        else :
            return None
    def show(self) :
        out = []
        if self.isFull() :
            out = self.List[self.front: ] + self.List[ :self.rear]
        elif not self.isEmpty() :
            if self.front < self.rear :
                out = self.List[self.front:self.rear]
            else :
                out = self.List[self.front: ] + self.List[ :self.rear]
        return out
    
Q = Queue(5)
Q.append(3)
Q.append(5)
Q.append(7)
Q.append(9)
Q.append(11)
print(Q.show())
print(Q.popleft())
print(Q.show())