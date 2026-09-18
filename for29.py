N = int(input())
K = int(input())
S = 0.0
for i in range(1, N + 1):
    S = S + i ** K
print(S)