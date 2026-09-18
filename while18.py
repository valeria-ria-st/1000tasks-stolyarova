N = int(input())
count = 0
S = 0
while N > 0:
    S = S + N % 10
    N = N // 10
    count = count + 1
print(count)
print(S)