from random import randint,choice



class pirat:
    pirats=[]
    polychil={"пустых":0,"болезни":0,"золото":0,"сундуков":0}
    count=0
    def __init__(self,name,load):
        self.name=name
        self.load=load
        if (load>60):
            self.load=randint(0,60)
        pirat.pirats.append(self)

    def vzal(self,nagr):
        while(self.load>=4):
            if (self.load<nagr.heaviness):
                return
            self.load-=nagr.heaviness
            self.polychil["сундуков"]+=1
            if(15>nagr.inside>0):
                self.polychil["болезни"]+=nagr.inside
            elif(nagr.inside>=15):
                self.polychil["золото"]+=nagr.inside
            else:
                self.polychil["пустых"]+=1


    def __str__(self):
        s=str(self.name)+" "+str(self.polychil)+"\n"
        return s


    def __It__(self,other):
        if(self.polychil[1]>other.polychil[1]):
            a={self.name:self.polychil[1]}
        elif(self.polychil[1]==other.polychil[1]):
            a={self.name:self.polychil[1],other.name:other.polychil[1]}
        else:
            a={other.name:other.polychil[1]}
        return(a)

    def __eq__(self,other):
        return(self.polychil[2]==other.zoloto[2])

    def pynkts():
        zoloto=[]
        illness=[]
        pusto=[]

        for i in pirat.pirats:
            zoloto.append(i.polychil["золото"])
            illness.append(i.polychil["болезни"])
            pusto.append(i.polychil["пустых"])
            print(i.name, " нашел сундуков ", i.polychil["сундуков"])

        for i in pirat.pirats:
            if(max(zoloto) == i.polychil["золото"]):
                print(i.name, "собрал больше всех монет = ", max(zoloto))

        for i in pirat.pirats:
            if(max(illness) == i.polychil["болезни"]):
                print(i.name, " дольше всех болел = " , max(illness))

        for i in pirat.pirats:
            if(min(pusto) == i.polychil["пустых"]):
                print(i.name, " собрал меньше всех пустых сундуков = ", min(pusto))






class chest:
    reward=[0,randint(3,10),randint(15,100)]
    def __init__(self):
        self.heaviness=randint(4,10)
        self.inside=choice(chest.reward)

Lous=pirat("Луис",150)
Vorob=pirat("Джек ворбей",40)
Black=pirat("Чёрная борода",50)
Monkey=pirat("Тарлан",25)

L=[Lous,Vorob,Black,Monkey]
for i in L:
    i.vzal(chest())
    print(i)
pirat.pynkts()









