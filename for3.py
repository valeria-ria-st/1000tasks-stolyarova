a = int(input("Введите число a:"))
b = int(input("Введите число b:"))


if a > b:
 a, b = b, a

count = 0

for i in range(b, a – 1, -1):
 print(i, end=' ')
 count += 1

print()
print("Количество чисел:", count)

