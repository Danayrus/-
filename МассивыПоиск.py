import random

massive = []
newMas = []
tempMas = []
l = int(input("Введите длину массива"))
r_1 = int(input("Введите начало диапазона"))
r_2 = int(input("Введите конец диапазона"))
num = int(input("Введите число"))
sh = 1
for k in range(l):
    r = random.randint(r_1, r_2)
    massive.append(r)
print("Начальный массив:" + str(massive))
print("================================")
print("Результат:")
for k in range(1, l):
    for i in range(2, l):
        if massive[k] + massive[i] == num:
            newMas.append(k)
            newMas.append(i)
            tempMas.append(newMas)
            # print(newMas)
            newMas = []
if len(tempMas) == 0:
    print("Нет нужных значений")
else:
    print(tempMas)



