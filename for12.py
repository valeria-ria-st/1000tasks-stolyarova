N = int(input())
P = 1.0
for i in range(1, N + 1):
    P = P * (1 + i / 10)
print(P)