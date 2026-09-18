X = float(input())
N = int(input())
S = X
P = X
for i in range(1, N + 1):
    P = P * (-1) * X * X / ((2 * i) * (2 * i + 1))
    S = S + P
print(S)