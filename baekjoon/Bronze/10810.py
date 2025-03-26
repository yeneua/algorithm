N, M = map(int, input().split())
basket = [0] * N

for _ in range(M):
    i, j, k = map(int, input().split())
    
    for s in range(j-i+1):
        basket[i+s-1] = k
    
print(*basket)
