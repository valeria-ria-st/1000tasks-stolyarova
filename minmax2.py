n = int(input())
mn = float('inf')
for _ in range(n):
    a = float(input())
    b = float(input())
    s = a * b
    if s < mn:
        mn = s
print(mn)