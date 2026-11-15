n = int(input())
x = int(input())
y = int(input())
a = [x, y]
for i in range(2, n):
    a.append(sum(a))
print(a)