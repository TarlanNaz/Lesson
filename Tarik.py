from math import sqrt


class Derror(BaseException):
    pass

try:
    a=int(input())
    b=int(input())
    c=int(input())
    D=(b**2)-(4*a*c)
    print(D)

    if D<0:
        raise Derror("Lox")
    if D==0:
        print((-b)/(2*a))
    if D>0:
        print("x1 =",(-b-sqrt(D))/(2*a))
        print("x2 =",(-b+sqrt(D))/(2*a))

except ZeroDivisionError:
    print("Коэфицента a должен быть > 0")

except ValueError:
    print("Коэфиценты должны быть числами или цифрами")

except Derror:
    print("Idi tyt")




