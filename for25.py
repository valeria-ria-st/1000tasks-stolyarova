X = float(input())
N = int(input())
S = 0.0
P = 1.0
for i in range(1, N + 1):
    P = P * (-X)
    S = S + P / i
print(S)