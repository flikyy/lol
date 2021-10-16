num=int(input("Введите число от 1 до 12: "))
cycles=int(10)
i=0
a=1
while i<cycles:
    if num<=12:
         print(num * a)
         a+=1
         i+=1
    
    else:
        print("ERROR;3")
        break

