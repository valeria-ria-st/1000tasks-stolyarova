N = int(input())
K = int(input())
chastnoe = 0
ostatok = N
while ostatok >= K:
    ostatok = ostatok - K
    chastnoe = chastnoe + 1
print(chastnoe)
print(ostatok)