a = int(input("Введите число a: "))
b = int(input("Введите число b: "))

if a > b:
    a, b = b, a  
for i in range(a, b + 1):
    print(i, end=' ')  
