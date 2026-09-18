P = float(input())
S = 0.0
d = 10.0
K = 0
while S <= 200:
    S = S + d
    d = d + d * P / 100
    K = K + 1
print(K)
print(S)