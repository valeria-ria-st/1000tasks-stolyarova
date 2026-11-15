a = [int(input()) for _ in range(10)]
r = 0
for x in a[:-1]:
    if x < a[-1]:
        r = x
        break
print(r)