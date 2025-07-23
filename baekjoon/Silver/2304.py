columns = [0 for _ in range(1001)]
max_column = (0, 0)
width = 0

N = int(input())

for _ in range(N):
    L, H = map(int, input().split())
    columns[L] = H
    
    if max_column[1] < H:
        max_column = (L, H)

current = 0
for i in range(1, max_column[0]+1):
    current = max(current, columns[i])
    width += current

current = 0
for i in range(1000, max_column[0], -1):
    current = max(current, columns[i])
    width += current
    
print(width)
