n = int(input())
mx = float('-inf')
for _ in range(n):
    a = float(input())
    b = float(input())
    p = 2 * (a + b)
    if p > mx:
        mx = p
print(mx)