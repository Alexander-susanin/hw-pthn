#stack using list
stackList = ["Engl", "Arab", "usa", "Bel"]
stackList.append("Rus")

print(stackList)
print(stackList.pop())
print(stackList)

#stack using Deque Collection
from collections import deque
stackStore = deque()
stackStore.append("Python")
stackStore.append('C++')
stackStore.append('Java')
print(stackStore)

stackStore.pop()
stackStore.pop()
print(stackStore)

#stack using LifoQueue
from queue import LifoQueue
stackMag = LifoQueue(maxsize = 8)
print(stackMag.qsize())

stackMag.put('1')
stackMag.put('3')
stackMag.put('5')
stackMag.put('7')
stackMag.put('9')

print("Is the stack full?: ", stackMag.full())
print("The size of the stack is: ", stackMag.qsize())
print(stackMag.get())
print(stackMag.get())
print(stackMag.get())
print(stackMag.get())
print('\nIs the stack empty?: ', stackMag.empty())