n = int(input())
a = [float(input()) for _ in range(n)]
print([2 * x if x < 5 else x / 2 for x in a])