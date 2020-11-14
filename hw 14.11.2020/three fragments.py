import random
list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
zam = 4
stroka = input("введите строку")
a = 0
b = 3
for i in stroka:
    for i in range(b):
        if a == 1 :
            print(random.choice(list), end='')
            a += 1
        elif a == zam:
            print(random.choice(list), end='')
            a += 1
            zam += 3
        else:
            print(stroka[a], end='')
            a += 1
    print("")