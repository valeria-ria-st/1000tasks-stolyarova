n = int(input())
mn = float('inf')
mx = float('-inf')
first_max = 0
last_min = 0
for i in range(1, n + 1):
    x = int(input())
    if x > mx:
        mx = x
        first_max = i
    if x <= mn:
        mn = x
        last_min = i
print(first_max, last_min)