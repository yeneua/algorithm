N = 9
heights = []

for _ in range(N):
    num = int(input())
    heights.append(num)

heights.sort()
total = sum(heights)

for i in range(N-1):
    for j in range(i+1, N):
        temp = total - heights[i] - heights[j]
        if temp == 100:
            idx = (i,j)
            break
for i in range(N):
    if i not in idx:
        print(heights[i])
