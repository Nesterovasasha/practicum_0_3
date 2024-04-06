X = int(input("Введите число X: "))
Y = int(input("Введите число Y: "))

result = (X % Y == 0) or (Y % X == 0)
print(1 if result else 0)