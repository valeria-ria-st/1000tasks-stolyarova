price = float(input("Введите цену за 1 кг конфет: "))
for weight in range(1, 11):
    cost = price * weight
    print(f"Стоимость {weight} кг: {cost}")
