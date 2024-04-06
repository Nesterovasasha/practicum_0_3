def convert_seconds_to_time(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return hours, minutes, seconds

user_input = int(input("Введите количество секунд (от 1 до 86400): "))

if 1 <= user_input <= 86400:
    hours, minutes, seconds = convert_seconds_to_time(user_input)
    print(f"Текущее время: {hours} часов, {minutes} минут, {seconds} секунд")
else:
    print("Введенное число должно быть в диапазоне от 1 до 86400")