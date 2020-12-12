import random 

list = [random.randint(0, 35) for i in range(random.randint(7, 35))]
print(list)
mx = 0
for elem in range(len(list)):
    if (elem + 1)%2 != 0:
        if list[elem]%3 == 0 and list[elem]>mx:
            mx = list[elem]
print(mx)