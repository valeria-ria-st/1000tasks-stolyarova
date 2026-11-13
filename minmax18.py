n = int(input())
mx = float('-inf')
first_max = 0
last_max = 0
for i in range(1, n + 1):
    x = int(input())
    if x > mx:
        mx = x
        first_max = i
        last_max = i
    elif x == mx:
        last_max = i
print(last_max - first_max - 1)