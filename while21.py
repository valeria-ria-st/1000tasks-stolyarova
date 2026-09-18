N = int(input())
i = 2
is_prime = True
while i * i <= N:
    if N % i == 0:
        is_prime = False
    i = i + 1
print(is_prime)