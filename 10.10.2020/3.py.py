def north(cmd):
#задаем функцию для north
    global position
#global как глобальная переменная (доступная в любом месте программы)
    if cmd == 0:
        position = 11
        print("North")
    elif cmd == 1:
        position = 12
        print("West")
    elif cmd == -1:
        position = 14
        print("East")
    else:
        print("error")
 
 
def west(cmd):
#функция для west
    global position
    if cmd == 0:
        position = 12
        print("West")
    elif cmd == 1:
        position = 13
        print("South")
    elif cmd == -1:
        position = 11
        print("North")
    else:
        print("error")
 
 
def south(cmd):
#функция для south
    global position
    if cmd == 0:
        position = 13
        print("South")
    elif cmd == 1:
        position = 14
        print("East")
    elif cmd == -1:
        position = 12
        print("West")
    else:
        print("error")
 
 
def east(cmd):
#функция для east
    global position
    if cmd == 0:
        position = 14
        print("East")
    elif cmd == 1:
        position = 11
        print("North")
    elif cmd == -1:
        position = 13
        print("South")
    else:
        print("error")
 
 
def light_coordinates(my_command):
    global position
    if position == 11:
        north(my_command)
    elif position == 12:
        west(my_command)
    elif position == 13:
        south(my_command)
    elif position == 14:
        east(my_command)
 
 
def main():
#функция основного
    while True:
#наш "бесконечный цикл"
        print("Command: 0 = continue movement, 1 = turn left, -1 = turn right")
        my_command = int(input("Enter command: "))
        light_coordinates(my_command)
 
 
print("Position: 11 = North, 12 = West, 13 = South, 14 = East")
position = int(input("Enter first position: "))
main()