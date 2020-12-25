class MyQueue:
    def __init__(self):
        self.instack = []
        self.outstack = []
    
    def push(self, elem):
        self.instack.append(elem)
    
    def pop(self):
        if not self.outstack:
            while self.instack:
                self.outstack.append(self.instack.pop())
        return self.outstack.pop()

    def size1(self):        
        return (len(self.instack))

    def size2(self):         
        return (len(self.outstack))

q = MyQueue()
for i in range(10):
    q.push(i)
for i in range(5):
    print(q.push(i))
    print(q.pop())
print('The size of the first stack: ', q.size1())
print('The size of the second stack: ', q.size2())
