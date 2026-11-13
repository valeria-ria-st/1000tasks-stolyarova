n = int(input())
prev = int(input())
start = 1
cur_len = 1 if prev == 1 else 0
best_start = 0
best_len = 0
for i in range(2, n + 1):
    x = int(input())
    if x == prev and x == 1:
        cur_len += 1
        if cur_len >= best_len and best_len > 0:
            best_len = cur_len
            best_start = start
    elif x == 1:
        start = i
        cur_len = 1
        if cur_len > best_len:
            best_len = cur_len
            best_start = start
    else:
        cur_len = 0
    prev = x
if prev == 1 and cur_len > best_len:
    best_len = cur_len
    best_start = start
if best_len == 0:
    print(0, 0)
else:
    print(best_start, best_len)