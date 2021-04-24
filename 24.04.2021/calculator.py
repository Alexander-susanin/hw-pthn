import sys
import math

while True:
	try:
		num1, operation, num2 = [i for i in input(
'''\nEnter math expression (num1 operation num2): 
U can use the operations: '0' to exit, '+', '-', '*', '/', '**', 
'sqrt'(write num sqrt 1), 'sin', 'cos', 'tan'(write num (sin, cos, tan) 1), 
''').split()]
	except ValueError:
		print('Invalid input! Try again')
		continue
	num1 = int(num1)
	num2 = int(num2)

	if operation == '0':
		sys.exit()#we can use break
	
	elif operation == '+':
		print(f'{num1} {operation} {num2} = {num1 + num2}')
	
	elif operation == '-':
		print(f'{num1} {operation} {num2} = {num1 - num2}')
	
	elif operation == '*':
		print(f'{num1} {operation} {num2} = {num1 * num2}')
	
	elif operation == '/':
		try:
			print(f'{num1} {operation} {num2} = {num1 / num2}')
		except ZeroDivisionError:
			print('Error. U cannot divide by zero')
	
	elif operation == '**':
		print(f'{num1} {operation} {num2} = {math.pow(num1, num2)}')
	
	elif operation == 'sqrt':
		print("Write the number to extract it's root like: num sqrt 1")
		print(f'{num1} {operation} = {math.sqrt(num1)}')
	
	elif operation == 'sin':
		print("Write the number to sin it like: num sin 1")
		print(f'{num1} {operation} = {math.sin(num1)}')

	elif operation == 'cos':
		print("Write the number to cos it like: num cos 1")
		print(f'{num1} {operation} = {math.cos(num1)}')

	elif operation == 'tan':
		print("Write the number to tan it like: num tan 1")
		print(f'{num1} {operation} = {math.tan(num1)}')