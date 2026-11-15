n = int(input())
a = [int(input()) for _ in range(n)]
b = a[::2]
print(len(b), b)