N = int(input())
found = False
while N > 0:
    if N % 10 == 2:
        found = True
    N = N // 10
print(found)