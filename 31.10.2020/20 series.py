import random

series = 1
summa_series = 0
amount_1 = 0
amount_2 = 0
length = 0
average_number_2 = 0
average_length = 0
max_notzero = 0
notzero = 0
#создаем переменные
while series != 21:
    print("This is ", series, "series")
    #цикл для генерации 20 серий
    while summa_series != 12:
        random_number = random.randint(0, 2)
        #цикл для генерации 20 серий из 0, 1, 2(в рандоме), но сумма чисел для каждой новой строки не превышает 12
        if (summa_series + random_number <= 12):
            print(random_number, end="")
            summa_series += random_number
            length += 1
            average_length += 1
            if (random_number == 1):
                amount_1 += 1
            elif (random_number == 2):
                amount_2 += 1
                average_number_2 += 1
            if (random_number != 0):
                notzero += 1

    print("Numder of units in da series: ", amount_1)
    print("Numder of twins in da series: ", amount_2)
    print("Da length of da series: ", length)
    print("=========================")
    if (notzero > max_notzero):
        max_notzero = notzero
    series += 1
    summa_series = 0
    amount_1 = 0
    amount_2 = 0
    length = 0
    notzero = 0
print("Average number of two: ", average_number_2/20)
print("Average length: ", average_length/20)
print("Da largest amount of non-zero number: ", max_notzero)
#итог для всех 20 серий