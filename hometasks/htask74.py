colors = ["red", "blue", "black", "white", "grey","brown", "purple","green","yellow"]

num1 = int(input("Введите любое число от 0 до 4: "))
num2 = int(input("Введите любое число от 5 до 9: "))

if num1 >= 0 and num1 < 5 and num2 >=5 and num2 <10:
    for i in range(num1, num2):
        print(colors[i])
else:
    print("ERROR!!!")        
