n = int(input())
a = [int(input()) for _ in range(n)]
b = [x for x in a if x % 2 != 0]
print(b, len(b))