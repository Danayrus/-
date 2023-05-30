
def one():
    massive = []
    massivein = []
    print("Введите размер массива")
    n1 = int(input("n = "))
    nn = n1-1
    for k in range(n1):
        massive.append([])
        for i in range(n1):
            if i == nn - k:
                massive[k].append(1)
            if i < nn - k:
                massive[k].append(0)
            if i > nn - k:
                massive[k].append(2)
    massiveAns = ""
    for i in range(len(massive)):
        for j in range(len(massive[i])):
            massiveAns += str(massive[i][j]) + " "
        massiveAns +="\n"
    return print(massiveAns)

def two():
    massive = []
    n1 = 2
    while n1%2 == 0:
        print("Введите нечетный размер массива")
        n1 = int(input("n = "))
    nn = n1 - 1
    for k in range(n1):
        massive.append([])
        for i in range(n1):
            massive[k].append(".")

    l = (len(massive)-1)/2

    for i in range(len(massive)):
        for j in range(len(massive[i])):
            if i == j:
                massive[i][j] = "*"
            if j == len(massive) - i - 1:
                massive[i][j] = "*"
            if i == l or j == l:
                massive[i][j] = "*"
    massiveAns = ""
    for i in range(len(massive)):
        for j in range(len(massive[i])):
            massiveAns += str(massive[i][j]) + " "
        massiveAns += "\n"
    return print(massiveAns)

def three():
    massive = []
    print("Введите размер массива")
    n1 = int(input("n = "))
    for k in range(n1):
        massive.append([])
    for i in range(len(massive)):
        for j in range(len(massive)):
            massive[i].append(abs(i - j))
    massiveAns = ""
    for i in range(len(massive)):
        for j in range(len(massive[i])):
            massiveAns += str(massive[i][j]) + " "
        massiveAns += "\n"
    return  print(massiveAns)
while True:
    answer = input("Введите номер задания")
    if answer == "1":
        print(one())
    elif answer == "2":
        print(two())
    elif answer == "3":
        print(three())
    else:
        print("Нет такого задания")
    answer = input("Хотите выбрать другое задание? 1. Да 2. Нет")
    if answer == "2":
        break
    elif answer != "1":
        break
