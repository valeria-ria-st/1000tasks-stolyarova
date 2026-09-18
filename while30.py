eps = float(input())
A1 = 1.0
A2 = 2.0
K = 3
A3 = (A1 + 2 * A2) / 3
while abs(A3 - A2) >= eps:
    A1 = A2
    A2 = A3
    A3 = (A1 + 2 * A2) / 3
    K = K + 1
print(K)
print(A2)
print(A3)