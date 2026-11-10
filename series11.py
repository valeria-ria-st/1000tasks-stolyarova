k = int(input())
idx = 0
i = 0
while True:
    x = int(input())
    if x == 0:
        break
    i += 1
    if x > k:
        idx = i
print(idx)