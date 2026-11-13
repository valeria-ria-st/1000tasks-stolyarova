n = int(input())
mn = float('inf')
for _ in range(n):
    x = float(input())
    if x > 0 and x < mn:
        mn = x
if mn == float('inf'):
    print(0)
else:
    print(mn)