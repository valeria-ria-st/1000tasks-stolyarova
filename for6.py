price = float(input("Введите цену за 1 кг конфет: "))
for i in range(12, 21, 2):
    weight = i / 10.0
    cost = price * weight
    print(f"Стоимость {weight} кг: {cost}")
