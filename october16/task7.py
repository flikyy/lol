name=str(input("Введите имя пользователя: "))
num=int(input("Введите число до 10: "))
cycles=num
i=0

while i<cycles:
    if cycles<=10:
        print(name)
        i+=1
    else:
        print('''
    Too high
    Too high
    Too high
    ''')
        break
       
        