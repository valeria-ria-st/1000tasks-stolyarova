eps = float(input())
A_prev = 2.0
A_cur = 2 + 1 / A_prev
K = 2
while abs(A_cur - A_prev) >= eps:
    A_prev = A_cur
    A_cur = 2 + 1 / A_prev
    K = K + 1
print(K)
print(A_prev)
print(A_cur)