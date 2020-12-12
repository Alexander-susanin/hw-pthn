#1 вариант
import random

class Queue:
 
    def __init__(self):
        self.items = []

    def isEmpty(self):      #Сравниваем с пустым листом. (True/False)
        return self.items == []
 
    def push(self, v):      #Добавляем в конец новый элемент
        self.items.append(v)   
 
    def pop(self):          #Извлекаем 1йы элемент
        element = self.items.pop()
        return element

    def size(self):         #Определяем размер очереди
        return (len(self.items))

    def printqueue(self):
        for items in self.items:
            print(items)

q = Queue()
print(q.isEmpty())
for i in range(random.randint(5, 10)):
    q.push(random.randint(0, 10))
print("All: ", q.size())
q.printqueue()
print("Последний: ", q.pop())
print("\n")

#2 вариант 
class Queue:

    def __init__(self):
        self._queue = []

    def push(self, x):
        self._queue.append(x)

    def pop(self):
        try:
            return self._queue.pop(0)
        except IndexError:
            return "Queue is empty."

    def peek(self):
        try:
            return self._queue[0]
        except IndexError:
            return "Queue is empty."

    def count(self):
        return len(self._queue)

someQueue = Queue()
for i in range(10):
    someQueue.push(i)

print(someQueue.pop())
print(someQueue.peek())