word = input("Введите ваше слово").lower()
wordTwo = word[::-1]
print(wordTwo)
if wordTwo == word:
    print("Ваше слово является палиндромом")
else:
   print("Ваше слово не является палиндромом")
n=1
a=1
s = int(input("Введите размер массива"))
massive = []
newMassive = []
tempMas=[]
for k in range(s):
    massive.append([])
    for i in range(s):
        massive[k].append(n)
        n += 1
for i in massive:
    print(i)
for k in range(len(massive)):
    for i in range(len(massive)):
        newMassive.append(massive[i][len(massive) - 1 - k])
    tempMas.append(newMassive)
    newMassive = []
        #print(tempMas)
print("===================================")
for i in tempMas:
    print(i)