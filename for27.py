X = float(input())
N = int(input())
S = X
num = 1.0
den = 1.0
for i in range(1, N + 1):
    num = num * (2 * i - 1) * X * X
    den = den * (2 * i) * (2 * i + 1)
    S = S + num / den
print(S)