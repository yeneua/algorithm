paper = [[0] * 100 for _ in range(100)]

N = int(input())
count = 0
for _ in range(N):
    x, y = map(int, input().split())
    
    for i in range(99-(y+10), 99-y):
        for j in range(x, x+10):
            if paper[i][j] == 0:
                paper[i][j] = 1
                count += 1

print(count)
