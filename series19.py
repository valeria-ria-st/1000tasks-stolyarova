n = int(input())
prev = None
for i in range(n):
    x = int(input())
    if i == 0 or x != prev:
        print(x)
        prev = x