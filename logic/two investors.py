summa=int(input("Минимальная сумма инвестиций - "))
maikl=int(input("Cколько $ у Майкла - "))
ivan=int(input("Сколько $ у Ивана - "))

if (maikl>=summa) and (ivan>=summa):
    print(2)
elif (maikl>=summa) and (ivan<=summa):
    print("Mike")
elif (maikl<=summa) and (ivan>=summa):
    print("Ivan")
elif (maikl<=summa) and (ivan<=summa) and ((maikl+ivan)>=summa):
    print(1)
elif (maikl<=summa) and (ivan<=summa) and ((maikl+ivan)<=summa):
    print(0)