n = int(input())
m1 = float('inf')
m2 = float('inf')
for _ in range(n):
    x = float(input())
    if x < m1:
        m2 = m1
        m1 = x
    elif x < m2:
        m2 = x
print(m1, m2)