n =int(input("Введите число: "))
for i in range(2, n):
    c = 0
    for j in range(1, int(i // 2) + 1):
        if i % j == 0:
            c += j
    if c == i:
        print("Совершённые числа: ",i)