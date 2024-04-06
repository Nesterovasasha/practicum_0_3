def get_third_digit_from_right(price_in_rubles):
    price_str = str(price_in_rubles)
    if len(price_str) >= 3:
        third_digit = price_str[-3]
        return third_digit
    else:
        return "Недостаточно цифр"

bitcoin_price = float(input("Введите стоимость биткоина в рублях: "))
third_digit = get_third_digit_from_right(bitcoin_price)

print(f"Цифра на третьей позиции справа: {third_digit}")