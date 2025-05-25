N , K = map(int, input().split())

top = 1
bottom = 1

for i in range(N, N-K, -1):
    top *= i

for j in range(K, 0, -1):
    bottom *= j

print(top//bottom)
