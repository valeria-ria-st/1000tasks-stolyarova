n = int(input())
mn = float('inf')
mx = float('-inf')
first_min = 0
last_max = 0
for i in range(1, n + 1):
    x = int(input())
    if x < mn:
        mn = x
        first_min = i
    if x >= mx:
        mx = x
        last_max = i
print(first_min, last_max)