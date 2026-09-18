A = float(input())
K = 0
S = 0.0
while S + 1 / (K + 1) < A:
    K = K + 1
    S = S + 1 / K
print(K)
print(S)