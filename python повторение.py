from random import randint
text="Антон Дмитривиевич сказал Я устал ждать я решаю В этот момент лицеисты 64 лицея напряглись"
L=[text.split(" ")]
a="0"
for i in L:
    if(len(a)<len(i)):
        a=i
print(a)
