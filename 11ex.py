N = float(input("Введите угол поворота часовой стрелки: "))

hours = int(N // 30)
minutes_angle = N % 30
minutes = int(minutes_angle * 2)

print("Полных часов прошло:", hours)
print("Полных минут прошло:", minutes)