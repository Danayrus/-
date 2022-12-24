a=0
b=0
print("Введите 15 чисел")
for i in range (15):
    c=int(input())
    if c>0:
        a=a+c
    elif c<0:
        b=b+c
print("Сумма положительных чисел равна: " + str(a))
print("Сумма отрицательных чисел равна: " + str(b))
