from random import randint
class Animal:
    def __init__(self,name,age):
        self.name=name
        self.age=age

class Predator(Animal):
    def bit(self,victim):
        if isinstance(victim,Mammal):
            if(victim.age<=self.from_what_age):
                Mammal.die(victim)
                #print (self.name, "Съел", victim.name)
                self.Happiness=True
                exit
            #else:
                #print(victim.name, "Убежал от", self.name)


class Mammal(Animal):
    def die(self):
        del self



class Tiger(Predator):
    def __init__(self,name,age,from_what):
        super().__init__(name,age)
        self.Happiness=False
        self.from_what_age=from_what


class Zebra(Mammal):
 pass



Zebros=list()

for i in range(3):
    Zebros.append(Zebra("Zebra",randint(1,30)))



Tigers=list()

for j in range(3):
    Tigers.append(Tiger("Tiger",randint(1,16),randint(1,30)))




for i in Tigers:
    for j in Zebros:
        Predator.bit(i,j)

for i in Tigers:
    if(i.Happiness==True):
        print("Тигр наелся")
    else:

        print("Тигр умер")



