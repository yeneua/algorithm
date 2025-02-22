numbers = [list(map(int, input().split())) for _ in range(9)]

max_num = numbers[0][0]
r = c = 0

for i in range(9):
    for j in range(9):
        if max_num < numbers[i][j]:
            max_num = numbers[i][j]
            r,c = i,j

print(f'{max_num}\n{r+1} {c+1}')
