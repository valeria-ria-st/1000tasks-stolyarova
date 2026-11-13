n = int(input())
prev = int(input())
start = 1
cur_len = 1
best_start = 1
best_len = 1
for i in range(2, n + 1):
    x = int(input())
    if x == prev:
        cur_len += 1
    else:
        if cur_len > best_len:
            best_len = cur_len
            best_start = start
        start = i
        cur_len = 1
    prev = x
if cur_len > best_len:
    best_len = cur_len
    best_start = start
print(best_start, best_len)