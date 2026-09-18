X = float(input())
N = int(input())
S = 1.0 + X / 2
num = 1.0
den = 2.0
for i in range(2, N + 1):
    num = num * (2 * i - 3) * X
    den = den * (2 * i)
    S = S + ((-1) ** (i - 1)) * num / den
print(S)