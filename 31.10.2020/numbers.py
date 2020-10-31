numbers = [22, 55, 77, 99, 88, 11, 33, 44, 66] 
n = 1 
while n < len(numbers):
	for i in range(len(numbers)-n):
		if numbers[i] > numbers[i+1]:
			numbers[i],numbers[i+1] = numbers[i+1],numbers[i]
	n += 1
print(numbers)