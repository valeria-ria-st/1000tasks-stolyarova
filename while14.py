N = int(input())
K = 0
S = 0
while S + K + 1 <= N:
    K = K + 1
    S = S + K
print(K)
print(S)