b = float(input())
c = float(input())
mx = float('-inf')
idx = 0
for i in range(1, 11):
    x = float(input())
    if b < x < c and x > mx:
        mx = x
        idx = i
if idx == 0:
    print(0, 0)
else:
    print(mx, idx)