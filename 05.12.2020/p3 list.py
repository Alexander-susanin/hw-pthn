import random 

list = [random.randrange(-10, 100) for i in range(10)]#создаем список
print([j for j in list if j%2])#с нечетными числами
mx = 0
for i in range(len(list)):
	if list[i%3 == 0] > list[mx]:
		mx = i
print(list[mx])