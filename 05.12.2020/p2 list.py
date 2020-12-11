import random

List = [random.randrange(-10, 10) for j in range(10)]#создаем список
print(List)

def mostFrequent(List):
    counter = 0
    num = List[0]     
    for i in List:
        currFrequency = List.count(i)
        if currFrequency > counter:
            counter = currFrequency
            num = i 
    return num 

print(mostFrequent(List))