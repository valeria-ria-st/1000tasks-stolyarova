N = int(input())
A1 = 1.0
A2 = 2.0
print(A1)
if N > 1:
    print(A2)
for i in range(3, N + 1):
    A1, A2 = A2, (A1 + 2 * A2) / 3
    print(A2)