num = int(input("Введите число: "))
if num > 1:
      for i in range(2,num):
              if (num % i) == 0:
                      print(num,"не простое")
                      break
      else:
              print(num,"простое")
 
else:
   print(num,"не простое")



