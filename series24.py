n = int(input())
cur = 0
sum_between = 0
for i in range(n):
    x = int(input())
    if x == 0:
        sum_between = cur
        cur = 0
    else:
        cur += x
print(sum_between)