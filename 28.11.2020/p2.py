text = input('Введите текст: ')
part_1 = text[0:(len(text))//2]
part_2 = text[len(text)//2:]
cipher = ''.join(i + j for i, j in zip(part_1, part_2))
print(cipher)
s3 = ''
s4 = ''
i = 0
while i < len(cipher):
    if i%2 == 0:
        s3 = s3 + cipher[i]
    else:
        s4 = s4 + cipher[i]
    i += 1
decipher = s3 + s4
print(decipher)