price_and_sales = input("Введите стоимость чашки латте в рублях и копейках и количество заказов за день последовательно через пробел: ")
x, y, n = map(int, price_and_sales.split())
total_price = (x * 100 + y) * n
rubles = total_price // 100
kopecks = total_price % 100
print(f"{rubles} руб. {kopecks} коп.")
