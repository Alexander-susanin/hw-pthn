import random
n = int(input("Кол-во игр:"))
win=0
lose=0
draw=0
for i in range (n) :
        a = int(input("1-камень, 2-ножницы, 3 -бумага: "))
        b = random.randint(1, 3)
        if a == b:
            print("ничья")
            draw += 1
        elif a == 1 and b == 2:
            print("победа")
            win += 1
        elif a == 1 and b == 3:
            print("поражение")
            lose += 1
        elif a == 2 and b == 1:
            print("поражение")
            lose += 1
        elif a == 2 and b == 3:
            print("победа")
            win += 1
        elif a == 3 and b == 1:
            print("победа")
            win += 1
        elif a == 3 and b == 2:
            print("поражение")
            lose += 1
print("побед",win, "поражений",lose, "ничья",draw)