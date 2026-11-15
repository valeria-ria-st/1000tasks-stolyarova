a = [int(input()) for _ in range(10)]
r = 0
for i in range(1, 9):
    if a[0] < a[i] < a[-1]:
        r = i + 1
print(r)