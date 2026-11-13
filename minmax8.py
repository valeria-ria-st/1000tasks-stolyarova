n = int(input())
mn = float('inf')
first_min = 0
last_min = 0
for i in range(1, n + 1):
    x = int(input())
    if x < mn:
        mn = x
        first_min = i
        last_min = i
    elif x == mn:
        last_min = i
print(first_min, last_min)