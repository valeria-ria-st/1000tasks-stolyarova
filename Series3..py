import random

arr = []
for i in range(10):
  arr.append(random.randint(1, 10))
print(arr)
sum = 0
for i in arr:
  sum += i
print("среднее арифметическое:", sum / len(arr))