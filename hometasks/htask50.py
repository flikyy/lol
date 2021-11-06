num=int(input("Введите число от 10 до 20 "))
while num < 10 or num > 20:
    if num <10:
        print("Too low")
    elif num > 20:
        print("Too high")
    ask=str(input("Хотите повторить попытку? y/n  "))
    if ask == "y":
        num=int(input("Введите число от 10 до 20"))
    else:
        print("Game Over!!!")
        break
        
if num > 10 and num <20:
    print("Thank you!")