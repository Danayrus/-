import random
def f1(s,c):
    spisok1 = []
    spisok2 = []
    spisok3 = []
    for i in range(s):
        r = random.randint(-100, 100)
        spisok1.append(r)
    for i in range(c):
        d = random.randint(-100, 100)
        spisok2.append(d)

    print("Массив1" + str(spisok1))
    print("Массив2" + str(spisok2))
    for i in range(len(spisok1)):
        q = int(spisok1[i]) % 2
        if (q != 0):
            spisok3.append(spisok1[i])
    for i in range(len(spisok2)):
        q = int(spisok2[i]) % 2
        if (q == 0):
            spisok3.append(spisok2[i])
    return spisok3
def f2(s):
    spisok = []
    spisok1 = []
    for i in range(s):
        r = random.randint(-100, 100)
        spisok.append(r)
    print("Массив\n" + str(spisok))
    for i in spisok[::-1]:
        spisok1.append(i)
    return spisok1
def f3(s,c):
    spisok = []
    spisok1 = []
    k = 0
    spisok.append(s)
    count=(c-s)+1
    for i in range(1,count):
        s+=1
        spisok.append(s)
    print(spisok)
    for i in range(len(spisok)):
        for j in range(2,c):
            if (spisok[i] % j ==0):
                k+=1
        if (k==1):
            spisok1.append(spisok[i])
        else:
            k=0
    return spisok1
def f4():
    return
def f4_1(x):
    return
def f5(s,c):
    spisok1 = []
    spisok2 = []
    spisok3 = []
    for i in range(s):
        r = random.randint(-10, 10)
        spisok1.append(r)
    for i in range(c):
        d = random.randint(-10, 10)
        spisok2.append(d)
    for i in range(len(spisok1)):
        spisok3.append(spisok1[i])
    print("Массив1" + str(spisok1))
    print("Массив2" + str(spisok2))
    print("Массив3" + str(spisok3))
    for i in range(len(spisok2)):
        n = int(spisok2[i])
        for j in range(len(spisok1)):
            if (n == int(spisok1[j])):
                del spisok3[j]
    return spisok3
print("задание")
ans = int(input())
if (ans == 1):
    print("Введите желаемое количество чисел в массиве 1")
    s = int(input())
    print("Введите желаемое количество чисел в массиве 2")
    c = int(input())
    print(f1(s, c))
if(ans == 2):
    print("Введите желаемое количество чисел в массиве")
    s = int(input())
    print(f2(s))
if(ans==3):
    print("Введите от")
    s = int(input())
    print("Введите до")
    c = int(input())
    print(f3(s, c))
if (ans==5):
    print("Введите желаемое количество чисел в массиве 1")
    s = int(input())
    print("Введите желаемое количество чисел в массиве 2")
    c = int(input())
    print(f5(s, c))




