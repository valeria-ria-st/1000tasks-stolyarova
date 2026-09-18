P = float(input())
S = 1000.0
K = 0
while S <= 1100:
    S = S + S * P / 100
    K = K + 1
print(K)
print(S)