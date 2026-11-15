n = int(input())
a = [int(input()) for _ in range(n)]
print(sum(1 for i in range(n) for j in range(i + 1, n) if a[i] > a[j]))