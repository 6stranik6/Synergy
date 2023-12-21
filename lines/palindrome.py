string = input("Ввидите слово ")
string = string.lower()
if string == string[::-1]:
    print("yes")
else:
    print("no")