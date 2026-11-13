n = int(input())
mn = float('inf')
mx = float('-inf')
first_extr = 0
for i in range(1, n + 1):
    x = int(input())
    if x < mn:
        mn = x
        if first_extr == 0:
            first_extr = i
    if x > mx:
        mx = x
        if first_extr == 0:
            first_extr = i
print(first_extr)