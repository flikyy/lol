a=("Russia","Belarus","America","Japan","Ukraine")
s=tuple(a)
print(s)
ask=str(input("Введите название любой страны из перечисленных выше: "))
if ask == "Russia":
    print("Индекс страны равен 1")
elif ask == "Belarus":
    print("Индекс страны равен 2")    
elif ask == "America":
    print("Индекс страны равен 3")    
elif ask == "Japan":
    print("Индекс страны равен 4") 
elif ask == "Ukraine":
    print("Индекс страны равен 5")
else:
    print("ERROR!!!!!")
           