X = float(input())
N = int(input())
S = 0.0
P = X
for i in range(1, N + 1):
    S = S + P / (2 * i - 1)
    P = P * (-1) * X * X
print(S)