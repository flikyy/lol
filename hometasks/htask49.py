compnum=int(50) 
att=int(1)
num=int(input("Введите число: "))
while num != compnum:
    if num < compnum:
        print("Ваше число меньше, числа которого загадали;3")
        att +=1
        num=int(input("Введите число: "))
    elif num > compnum:
        print("Ваше число больше, числа которого загадали;3")
        att+=1
        num=int(input("Введите число: "))
if num == compnum:
    print("Well done, you took",att,"attempts")    