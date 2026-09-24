import random

N = int(input("Введите число: "))

arr = []
for i in range(N):
  arr.append(random.randint(0, 10))
print(arr)
sum = 0
pr = 1
for i in arr:
  sum += i
  pr *= i
print("Сумма: ", sum)
print("Произведение:", pr )