N, K = map(int, input().split())
coins = []
count = 0

for _ in range(N):
    coins.append(int(input()))

coins.sort(reverse=True)

for i in range(N):
    if coins[i] <= K:
        while coins[i] <= K:
            count += 1
            K -= coins[i]

print(count)
