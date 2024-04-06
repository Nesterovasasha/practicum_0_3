numbers = input("Последовательно через пробед введите числа K, N, R: ")
K, N, R = map(int, numbers.split())
result = int(str(K) * N) * R
print(result)