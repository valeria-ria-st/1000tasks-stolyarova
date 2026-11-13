n = int(input())
prev = float(input())
mx = float('-inf')
for _ in range(n - 1):
    x = float(input())
    s = prev + x
    if s > mx:
        mx = s
    prev = x
print(mx)