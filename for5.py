price = float(input("Введите цену за 1 кг конфет: "))
for i in range(1, 11):
    weight = i / 10
    cost = price * weight
    print(f"Стоимость {weight} кг: {cost}")
