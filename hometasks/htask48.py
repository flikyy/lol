name=str(input("Введите имя человека, которого хотите позвать на вечиринку: "))
invm=1
s=str("")
otvet=str(input("Хотите пригласить ещё кого нибудь? y/n  "))

if otvet == "y":
    while otvet == "y":
        name=str(input("Введите имя человека, которого хотите позвать на вечиринку: "))
        invm+=1
        otvet=str(input("Хотите пригласить ещё кого нибудь? y/n  "))
        if otvet == "n":
            if invm == 1:
                print("Хорошо, вы приглосили ",invm," человека.")
            elif invm >1 or invm == 0:
                print("Хорошо, вы приглосили ",invm,"человек.")

elif otvet == "n":
    if invm == 1 or invm== 3:
        print("Хорошо, вы приглосили ",invm," человека.")
    elif invm >1 and invm<3 or invm == 0 or invm>3:
        print("Хорошо, вы приглосили ",invm,"человек.")
else:
    print("ERROR!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!;3")    
