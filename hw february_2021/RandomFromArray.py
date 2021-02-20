import random
		
counter = 0
values = [random.randint(1, 5) for i in range(1, 4)]
weight = [random.randint(0, 5) for i in range(1, 4)]
sum_weight = []
for i in range(len(values)):
	for j in range (int(weight[counter])):
		sum_weight += [(values[counter])]
	counter += 1
print('Два массива: ', values, weight)
print('Третий массив', sum_weight)
print(random.choice(sum_weight))