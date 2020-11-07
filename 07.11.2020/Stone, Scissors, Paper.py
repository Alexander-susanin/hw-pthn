import random
#Счетчики Ничьи, проигрышей, побед
CountDraw = 0
CountLose = 0
CountWin = 0
list = ['st','sc','p'] # Значения рандомной выборки - Камень, Ножницы, Бумага

def inp():
	global n
	while True:
		n = int(input("Введите количество игр n: "))
		return n

def logicGame(x, y):
	global CountDraw , CountLose, CountWin
	if x == y:
		print('Ничья')
		CountDraw += 1
	elif(x == 'st' and y == 'sc') or (x == 'sc' and y == 'p') or (x == 'p' and y == 'st'):
		print('Выигрыш')
		CountWin += 1
	else:
		print('Проигрыш')
		CountLose+= 1      
	return CountDraw, CountWin, CountLose

inp()
while n != 0:
    while True:
        x = input('Камень (st), Ножницы (sc), Бумага (p)')
        if x not in list:
            print('Введите st, sc, p')
        else: break

    y = random.choice(list)
    logicGame(x, y)
    n -= 1
else:
    print("Победы: ", CountWin, "Проигрыши: ", CountLose, "Ничьи:", CountDraw)
