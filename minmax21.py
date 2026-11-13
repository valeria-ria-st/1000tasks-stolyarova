n = int(input())
mn = float('inf')
mx = float('-inf')
s = 0
for _ in range(n):
    x = float(input())
    s += x
    if x < mn:
        mn = x
    if x > mx:
        mx = x
print((s - mn - mx) / (n - 2))