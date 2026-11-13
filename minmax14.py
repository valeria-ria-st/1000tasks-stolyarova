b = float(input())
mn = float('inf')
idx = 0
for i in range(1, 11):
    x = float(input())
    if x > b and x < mn:
        mn = x
        idx = i
if idx == 0:
    print(0, 0)
else:
    print(mn, idx)