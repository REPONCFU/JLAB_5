
# Ввод натурального числа
n = int(input("Enter a natural number (n): "))

# Вычисление частного и остатка
k = n // 7
r = n % 7

# Вывод результата
if r == 0:
    print(f"n = 7 * {k}")
else:
    print(f"n = 7 * {k} + {r}")
