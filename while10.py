N = int(input())
K = 1
while 3 ** (K + 1) < N:
    K = K + 1
print(K)