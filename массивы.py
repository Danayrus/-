import random
def one():
    massive = []
    k = 0
    prov = 2  ## prov = 1 - +, prov = 0 - -
    s = 0
    while True:
        r = random.randint(-1000, 1000)
        massive.append(r)
        if massive[k] == 0:
            break
        k += 1
    print("Начальный массив: " + str(massive))
    for i in range(len(massive)):
        if massive[i] >= 0 and prov != 1:  ## +
            prov = 1
            s += 1
        elif massive[i] <= 0 and prov != 0:  ## -
            prov = 0
            s += 1
    s -= 1
    return print("Знак поменялся " + str(s) + " раз")

# 2
def two():
    massive = []
    massivePlus = []
    massiveMinus = []
    plus = 0
    minus = 0
    itogPlus = 0
    itogMinus = 0
    k = 0
    while True:
        r = random.randint(-1000, 1000)
        massive.append(r)
        if massive[k] == -1000:
            break
        k += 1
    print("Начальный массив: " + str(massive))

    for i in range(len(massive)):
        if massive[i] >= 0:  ## +
            massivePlus.append(massive[i])
        elif massive[i] <= 0:  ## -
            massiveMinus.append(massive[i])

    print("Массив с положительными числами: " + str(massivePlus))
    print("Массив с отрицательными числами: " + str(massiveMinus))

    for i in range(len(massivePlus)):
        plus+=massivePlus[i]
    itogPlus = plus/len(massivePlus)

    for i in range(len(massiveMinus)):
        plus+=massiveMinus[i]
    itogMinus = plus/len(massiveMinus)
    return print ("Среднее арифметическое положительных чисел: " + str(itogPlus) +
                  "\nСреднее арифметическое отрицательных чисел: " + str(itogMinus))




def three():
    massive = []
    massive_2 = []
    answer = str
    unique = True
    count = 0
    l = int(input("Введите длину массива"))
    r_1 = int(input("Введите начало диапазона"))
    r_2 = int(input("Введите конец диапазона"))
    ll = l
    for i in range(l):
        r = random.randint(r_1, r_2)
        massive.append(r)
    print("Начальный массив: " + str(massive))
    while len(massive) !=0:
        ## Проверяем уникальность 0 числа
        for i in range(1, l):
            if l == 1:
                massive_2.append(massive[i])
            else:
                if massive[0] != massive[i]:
                    unique = True
                else:
                    unique = False
                    break
        ## Добавляем нулевой элемент
        if unique == True:
            massive_2.append(massive[0])
        massive.pop(0)
        l-=1
        count +=1
    if ll == len(massive_2):
        answer = "Все числа являются уникальными"
    else:
        answer = "Числа не уникальны"
    return print(answer)


def four():
    d = dict()
    mostlongWord = ""
    countWord = 0
    wordwithMaxCount = ""
    text = input("Введите текст: ").split()
    for i in text:
        if i in d:
            d[i] +=1
        else:
            d[i]=1
    for key,count in d.items():
        if len(mostlongWord) < len(key):
            mostlongWord = key
        if countWord < count:
            countWord = count
            wordwithMaxCount = key
    return print("Самое встречающееся слово: " + wordwithMaxCount + "\nСамое длинное слово: " +  mostlongWord)


while True:
    ans = input("Введите номер задания:\n1-знаки, 2 - среднее арифметическое,\n3 - уникальность чисел, 4 - текст")
    match ans:
        case "1":
            print(one())
        case "2":
            print(two())
        case "3":
            print(three())
        case "4":
            print(four())
    ans = input("Хотите продолжить? 1 - Да, 2 - Нет")
    if ans == "2":
        break
    elif ans != "1":
        break
    print("==========================================")
