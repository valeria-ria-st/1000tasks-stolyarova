n = int(input())
mn = float('inf')
mx = float('-inf')
last_extr = 0
for i in range(1, n + 1):
    x = int(input())
    if x <= mn:
        mn = x
        last_extr = i
    if x >= mx:
        mx = x
        last_extr = i
print(last_extr)