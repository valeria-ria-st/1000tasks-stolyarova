n = int(input())
a = [int(input()) for _ in range(n)]
for i in range(n):
    for j in range(i + 1, n):
        if a[i] == a[j]:
            print(i + 1, j + 1)
            exit()