from random import randint
class sq_matrix:
    def __init__(self,size,n):
        self.size=size
        self.num=n
        for g in range(n):
            self.L=[[randint(1,100)for j in range(size)]for i in range(size)]

    def __str__(self):
        return str(self.L)

    def glav(self):
        for i in range(self.size):
            sum=sum+int(self.L[i][i])
        return S



object1=sq_matrix(5,2)
print(object1)
object1.glav()

