A = int(input("Введите A: "))
B = int(input("Введите B: "))
total_sum = 0

for i in range(A, B + 1):
    total_sum += i
    
print(f"Сумма чисел от {A} до {B}: {total_sum}")

