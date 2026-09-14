A = int(input("Введите A: "))
B = int(input("Введите B: "))
product = 1

for i in range(A, B + 1):
    product *= i
    
print(f"Произведение чисел от {A} до {B}: {product}")

