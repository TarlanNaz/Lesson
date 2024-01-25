def Path(a):
    def OBA(V0,V,t):
        try:
            a(V0,V,t)
        except (TypeError,ZeroDivisionError):
            print("До свидания, Suka ebannay!")
            exit
        finally:
            print( (( ( V0 + V ) / 2 ) * t))
    return OBA



@Path
def a(V0,V,t):
    print((V-V0)/t)


V0=float(input())
V=float(input())
t=float(input())
print(a(V0,V,t))




