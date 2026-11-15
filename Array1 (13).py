n = int(input())
a = [int(input()) for _ in range(n)]
seen = set()
r = 0
for i, x in enumerate(a):
    if x < 1 or x > n or x in seen:
        r = i + 1
        break
    seen.add(x)
print(r)