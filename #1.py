#1
x1 = int(input("Введите число:"))
x2 = int(input("Введите число:"))
x3 = int(input("Введите число:"))
f = int(input("1 - Сумма\n2 - Разность\n"))
if f == 1:
    print(f"Сумма {x1 + x2 + x3}")
elif f == 2:
    print(f"Разность {x1 - x2 - x3}")