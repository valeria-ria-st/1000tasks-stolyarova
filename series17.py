n = int(input())
has_pos = False
for _ in range(n):
    if int(input()) > 0:
        has_pos = True
print(has_pos)