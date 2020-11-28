#Убирает все символы, не включая границы 
list1 = 'efrhrhe/*frefhjg/*tgtruteur*/egye'
words = ('/*', '*/')
print(list1[:list1.find(words[0]) + len(words[0])] + list1[list1.rfind(words[1]):])

#Убирает все символы, включая границы
list = 'This is a string /*here is a text to remove*/, and here is a text not to remove'
left = list.find('/*')
right = list.find('*/')

if left and right:
    new_list = list[:left] + list[right+1:]
    print(new_list)
