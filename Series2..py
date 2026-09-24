import random

arr = []
for i in range(10):
  arr.append(random.randint(1, 10))
print(arr)
proiz = 0
for i in arr:
  proiz *= i
print(proiz)
