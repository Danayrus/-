def min(a,b,c):
    if (a<b) & (a<c):
        m = a
    elif b<c:
        m = b
    else:
        m = c
    return m
def razr(a):
    i = 0
    while (a!=0):
        a = a // 10
        i = i + 1
    return i
def summ(N):
    s=0
    k=1
    for i in range(N):
       s=s+k
       k=k+1
    return s
def fact(a):
    t = 1
    s=1
    for i in range(a):
        t = t * s
        s = s + 1
    return t

print ("Какую опперацию вы хотите провести?\n(1-минимальное из трёх чисел;\n2-поиск колличества разрядов в числе;\n3-сумма чисел от 1 до N;\n4- Факториал числа N")
ans = int(input())
if ans==1:
    print ("Введите три числа")
    numb1= int(input())
    numb2= int(input())
    numb3= int(input())
    print (min(numb1,numb2,numb3))
elif ans==2:
    print("Введите число")
    numb1 = int(input())
    print (razr(numb1))
elif ans==3:
    print("Введите N")
    n= int(input())
    print (summ (n))
else:
    print("Введите N")
    n = int(input())
    print (fact (n))


