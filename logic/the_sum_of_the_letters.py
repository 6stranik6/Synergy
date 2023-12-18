slovo = input('Введите слово на английском языке: ')

ex = slovo.count('e')
ax = slovo.count('a') 
ix = slovo.count('i') 
ux = slovo.count('u') 
ox = slovo.count('o') 

schetglas=ex+ax+ix+ux+ox

print("Всего согласных",len(slovo)-schetglas)
print("Всего гласных",schetglas) 
if (ex==0):
    print ("гласной e в слове False")
else:
    print("e=",ex)
if (ux==0):
    print ("гласной u в слове False")
else:
    print("u=",ux)
if (ox==0):
    print ("гласной o в слове False")
else:
    print("o=",ox)
if (ax==0):
    print ("гласной a в слове False")
else:
    print("a=",ax)
if (ix==0):
    print ("гласной i в слове False")
else:
    print("i=",ix)