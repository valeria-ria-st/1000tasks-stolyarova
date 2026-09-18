N = int(input())
F1 = 1
F2 = 1
print(F1)
if N > 1:
    print(F2)
for i in range(3, N + 1):
    F1, F2 = F2, F1 + F2
    print(F2)