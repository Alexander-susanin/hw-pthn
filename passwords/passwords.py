import statistics
from statistics import mode

f = open('pwd.txt')
passwords = []
for line in f:
    passwords.append(line[line.find(';')+1:])
f.close()
ten = []
for i in range(10):
    ten.append(mode(passwords))
    for c in range(passwords.count(ten[i])):
    	passwords.remove(ten[i])		
print("TOP 10 Most popular passwords:")
for j in ten:
	print(j, end='')