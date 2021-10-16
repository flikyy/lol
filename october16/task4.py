name=str(input("Введите имя пользователя: "))
cycles=int(input("Введите кол-во повторений: "))

i=0

while i<cycles:
    for letter in name:
        print(letter)
    i+=1

