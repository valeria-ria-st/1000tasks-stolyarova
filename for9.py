A = int(input("Введите A: "))
B = int(input("Введите B: "))
sum_squares = 0

for i in range(A, B + 1):
    sum_squares += i ** 2
    
print(f"Сумма квадратов от {A} до {B}: {sum_squares}")

