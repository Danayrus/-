print("Введите число 1")
num1 = float(input())
print("Введите число 2")
num2 = float(input())
print("Если вы хотите вычислить квадратное уравнение, введите 3 число, иначе - введите операнд ")
answer = input()
print("Ответ:")
if answer == "+":
    print(num1 + num2)
elif answer == "-":
    print(num1 - num2)
elif answer == "*":
    print(num1 * num2)
elif answer == "/":
    print(num1 / num2)
else:
    answer = float(answer)
    D = float(num2**2 - (4*num1*answer))
    print("Дискриминант равен: " + str(D))
    if D<0:
        print("нет корней")
        exit()
    else:
        D = D ** 0.5
        x1 = str(((-1*num2) + D) / 2 * num1)
        x2 = str(((-1*num2) - D) / 2 * num1)
        if x1==x2:
            print("Уравнение имеет один корень\nx = " + x1)
        else:
            print("x1 = " + x1 + "\nx2 = " + x2)

