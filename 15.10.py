import random
def f1():
    n1 = (101 + 0) / 3
    print("№1\n" + str(n1))
    n2 = 3.0e-6 * 10000000.1
    print("№2\n" + str(n2))
    n3 = (True and True)
    print("№3\n" + str(n3))
    n4 = (False and True)
    print("№4\n" + str(n4))
    n5 = ((False and False) or (True and True))
    print("№5\n" + str(n5))
    n6 = ((False or False) and (True and True))
    print("№6")
    return n6

def f2(a,b,c,d):
    if (a == b) and (a == c) and (a == d):
        return ("Равно")
    else:
        return ("Не равно")
def f3(s,c):
    spisok = []
    spisok1 =[]
    for i in range(s):
        r = random.randint(-100, 100)
        spisok.append(r)
    print(spisok)
    for k in range(c):
        n = int(spisok[0])
        l=0
        for i in range(1,len(spisok)):
            if (n < int(spisok[i])):
                n = int(spisok[i])
                l=i
        spisok1.append(n)
        spisok[l] = -101
    return spisok1
def f4(s,c):
    spisok = []
    spisok1 = []
    for i in range(s):
        r = random.randint(-100, 100)
        spisok.append(r)
    print(spisok)
    for k in range(c):
        n = int(spisok[0])
        l = 0
        for i in range(1, len(spisok)):
            if (n > int(spisok[i])):
                n = int(spisok[i])
                l = i
        spisok1.append(n)
        spisok[l] = 101
    return spisok1
def f5(s):
    spisok = []
    spisok1 = []
    for i in range(s):
        r = random.randint(-100, 100)
        spisok.append(r)
    print(spisok)
    sr = int(spisok[0])
    for i in range(len(spisok)):
        sr = sr + int(spisok[i])
    sr /= s
    print("Среднее значение = " + str(sr))
    print("Числа больше среднего значения:")
    for i in range(len(spisok)):
        if (sr<int(spisok[i])):
            spisok1.append(spisok[i])
    return spisok1
def f6(h,l):
    r = h
    for i in range(1, l):
        h += r
    print("Ответ: ")
    return h
def f7(s):
    sp = []
    for i in range(s):
        r = random.randint(-100, 100)
        sp.append(r)
    print(sp)
    qq = []
    qqq = []
    for i in range(len(sp)):
        q = int(sp[i]) % 2
        if (q == 0):
            qq.append(sp[i])
        else:
            qqq.append(sp[i])
    print("четные числа:\n"+ str(qq))
    print("нечетные числа:")
    return qqq
def f8(F):
    C = (F - 32)/1.8
    print("Температура в Цельсиях:")
    return C
def f9(F,C):
    C = C / (F ** 2)
    print("Индекс массы тела:")
    return C
def f10(F):
    F3=F**4
    print("Квадрат числа:\n" + str(F ** 2) + "\nКуб числа:\n" + str(F ** 3))
    print("Четвертая степень числа:")
    return F3
def f11(a,b,c):
    if (a + b > c) and (b + c > a) and (a + c > b):
        return ("Можно составить треугольник")
    else:
        return ("Треугольник нельзя составить")
print ("Выберите задание:\n1 2\n3 4\n5 6\n7 8\n9 10\n11")
ans = int(input())
if (ans == 1):
    print("Задание 1:\n"+str(f1()))
elif(ans ==2):
    print("Задание 2:\nВведите 4 числа")
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    print(f2(a,b,c,d))
elif(ans ==3):
    print("Задание 3:\nВведите желаемое количество чисел в массиве")
    s = int(input())
    print("Введите желаемое количество чисел для вывода")
    c = int(input())
    if (c>s):
        print("Введено неправильное значение")
        exit()
    print(f3(s,c))
elif(ans ==4):
    print("Задание 4:\nВведите желаемое количество чисел в массиве")
    s = int(input())
    print("Введите желаемое количество чисел для вывода")
    c = int(input())
    if (c>s):
        print("Введено неправильное значение")
        exit()
    print(f4(s,c))
elif(ans ==5):
    print("Задание 5:\nВведите желаемое количество чисел в массиве")
    s = int(input())
    print(f5(s))
elif(ans==6):
    print("Задание 6:\nВведите числа для умножения")
    h = int(input())
    l = int(input())
    print(f6(h,l))
elif(ans==7):
    print("Задание 7:\nВведите желаемое количество чисел в массиве")
    s = int(input())
    print(f7(s))
elif(ans==8):
    print("Задание 8:\nВведите температуру в Форенгейтах")
    F = int(input())
    print(f8(F))
elif(ans==9):
    print("Задание 9:\nВведите рост и вес, рост введите как *.**")
    F = float(input())
    C = int(input())
    print(f9(F,C))
elif(ans==10):
    print("Задание 10:\nВведите число")
    F = int(input())
    print(f10(F))
elif(ans==11):
    print("Задание 11:\nВведите 3 числа")
    a = int(input())
    b = int(input())
    c = int(input())
    print(f11(a,b,c))
else:
    print("Такого задание нет")

