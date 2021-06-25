# 링크 큐
class Node :
    def __init__(self, value, prev, next) :
        self.value = value
        self.prev = prev
        self.next = next

class LinkedQueue:
    def __init__(self):
        self.Head = None
        self.Tail = None
        
    def append(self, value) :
        if self.Head is None :
            self.Head = Node(value, None, None)
            self.Tail = self.Head
        else :
            self.Tail.next = Node(value, self.Tail, None)
            self.Tail = self.Tail.next
            
    def popleft(self):
        if self.Head is None :
            return None 
        if self.Head == self.Tail :
            answer = self.Head.value
            self.Head = None
            self.Tail = None
            return answer
        
        answer = self.Head.value
        self.Head = self.Head.next
        self.Head.prev = None
        return answer
    
    def show(self) :
        s = '['
        
        curr = self.Head
        while curr is not None:
            s = str(curr.value) + ','
            curr = curr.next
            
        s += ']'
        print(s)

Q = LinkedQueue()
Q.append(1)