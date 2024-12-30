
# Ввод трёх действительных чисел
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
c = float(input("Enter the third number: "))

# Сортировка чисел
numbers = [a, b, c]
ascending_order = sorted(numbers)  # По возрастанию
descending_order = sorted(numbers, reverse=True)  # По убыванию

# Вывод результата
print(f"Numbers in ascending order: {ascending_order}")
print(f"Numbers in descending order: {descending_order}")
