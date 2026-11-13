n = int(input())
mn = float('inf')
mx = float('-inf')
for _ in range(n):
    x = float(input())
    if x < mn:
        mn = x
    if x > mx:
        mx = x
print(mn, mx)