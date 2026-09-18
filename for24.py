X = float(input())
N = int(input())
S = 1.0
P = 1.0
for i in range(1, N + 1):
    P = P * (-1) * X * X / ((2 * i - 1) * (2 * i))
    S = S + P
print(S)