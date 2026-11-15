n = int(input())
a = [int(input()) for _ in range(n)]
print(max(a.count(x) for x in set(a)))