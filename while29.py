A = float(input())
B = float(input())
C = float(input())
count = 0
while A >= C:
    B_temp = B
    while B_temp >= C:
        B_temp = B_temp - C
        count = count + 1
    A = A - C
print(count)