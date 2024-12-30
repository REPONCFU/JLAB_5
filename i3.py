
# Ввод начального количества клеток
initial_cells = int(input("Enter the initial number of amoeba cells: "))

# Количество делений за 6 часов (каждые 3 часа)
divisions = 6 // 3

# Вычисление общего числа клеток
final_cells = initial_cells * (2 ** divisions)

# Вывод результата
print(f"The number of cells after 6 hours: {final_cells}")
