import math

def calculate_angles(a, b, c):
    angle_A = math.degrees(math.acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c)))

    angle_B = math.degrees(math.acos((a ** 2 + c ** 2 - b ** 2) / (2 * a * c)))

    angle_C = 180 - angle_A - angle_B

    return angle_A, angle_B, angle_C


a = float(input('Введите сторону a: '))
b = float(input('Введите сторону b: '))
c = float(input('Введите сторону c: '))

angles = calculate_angles(a, b, c)
print(f'Угол A: {angles[0]:.2f} градусов')
print(f'Угол B: {angles[1]:.2f} градусов')
print(f'Угол C: {angles[2]:.2f} градусов')
