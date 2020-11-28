import itertools
text = "Отихтрудовлишьяодинбездомный"
part_1 = text[0:(len(text))//2]
part_2 = text[len(text)//2:]
res = ''.join(i + j for i, j in zip(part_1, part_2))
print(res)
