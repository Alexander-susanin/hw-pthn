import random

lst0 = [random.randrange(-10, 10) for x in range(10)]#создаем список
print(lst0)
max_lst = None
max_index = 0

for i in range(len(lst0) - 2):
   s = lst0[i] + lst0[i + 1] + lst0[i + 2]
   if (max_lst is None) or (s > max_lst):
      max_lst = s
      max_index = i

print('lst0[%s] + lst0[%s] + lst0[%s] = %s' % (max_index, max_index + 1, max_index + 2, max_lst), end='\n')