print("Введите числа. Если хотите решить квадратное уравнение, то введите 3 числа. После завершения ввода введите 'ок'")
spisok = []
ans = str
while ans != ('ок'):
    ans = input()
    spisok.append(ans)
spisok.pop()
print("Выберите интересующую вас операцию:\n'+' - сложение,\n'-' - вычитание,\n'*' - умножение,\n'/' - деление,\n'2' - решение квадратного уравнения")
oper = input()
def summ(s):
    ans = int(s[0])
    for i in range(1,len(s)):
        ans+=int(s[i])
    return ans

def sub(s):
    ans = int(s[0])
    for i in range(1,len(s)):
        ans-=int(s[i])
    return ans
def mult(m):
    ans = int(m[0])
    for i in range(1,len(m)):
        ans*=int(m[i])
    return ans
def div(d):
    if int(d[0]) == 0:
        ans = 0
    else:
        ans = int(d[0])
        for i in range(1, len(d)):
            if int(d[i]) == 0:
                ans = ("Нельзя делить на нуль")
            else:
                ans /= int(d[i])
    return ans
def quad(q):
    a,b,c = q
    a,b,c, = int(a),int(b),int(c)
    D = float((b**2) - (4 * a * c))
    if D < 0:
        ans = ("Нет корней")
    elif D == 0:
        ans = str(-b/(2*a))
    else:
        D = D**0.5
        x1 = str((-b + D) / (2 * a))
        x2 = str((-b - D) / (2 * a))
        ans = x1,x2
    return ans
if oper == "+":
    print("Сумма чисел равна:" + str(summ(spisok)))
elif oper == "-":
    print("Разница чисел равна:" + str(sub(spisok)))
elif oper == "*":
    print("Произведение чисел равно:" + str(mult(spisok)))
elif oper == "/":
    print("Частность чисел равна:" + str(div(spisok)))
elif oper == 2:
    print("Корни квадратного уравнения:\n" + str(quad(spisok)))
