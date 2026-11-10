k = int(input())
n = int(input())
has = False
for _ in range(n):
    if int(input()) < k:
        has = True
print(has)