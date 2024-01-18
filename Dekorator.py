from math import sqrt

def decorator(kv_kor):
    def wrapper(a,b,c):
        print("x1+x2=-b; x1*x2=c")
        kv_kor(a,b,c)
    return wrapper

@decorator
def kv_kor(a,b,c):
    D=b**2-(4*a*c)
    if(D<0):
        return ("Иди дискриминант по новой делай")
    if D==0:
        print((-b)/(2*a))
    else:
        D=sqrt(D)
        print("x1 =",(-b+D)/(2*a),' x2 =',(-b-D)/(2*a))




print(kv_kor(1,-5,4))

