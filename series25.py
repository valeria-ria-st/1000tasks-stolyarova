n = int(input())
first_zero = -1
sum_between = 0
for i in range(n):
    x = int(input())
    if x == 0:
        if first_zero == -1:
            first_zero = i
    elif first_zero != -1:
        sum_between += x
print(sum_between)