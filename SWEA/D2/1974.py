# 첫 번째 풀이
T = int(input())
 
for tc in range(1, T+1):
 
    sudoku = []
 
    for _ in range(9):
        numbers = list(map(int, input().split()))
        sudoku.append(numbers)
 
    row_sum = 0
    col_sum = 0
    square_sum = 0
    result = 1
 
    for i in range(9):
        row_sum= 0
        col_sum = 0
        for j in range(9):
            row_sum += sudoku[i][j]
            col_sum += sudoku[j][i]
        if row_sum != 45 or col_sum != 45:
            result = 0
            break
     
    for i in range(0,9,3):
        for j in range(0,9,3):
            square_sum = 0
            for x in range(i,i+3):
                if x % 2:
                    for y in range(j+2, j-1, -1):
                        square_sum += sudoku[x][y]
                else:
                    for y in range(j, j+3):
                        square_sum += sudoku[x][y]
 
            if square_sum != 45:
                result = 0
                break
             
 
    print(f'#{tc} {result}')


# 두 번째 풀이
T = int(input())

for tc in range(1, T+1):

    sudoku = []

    for _ in range(9):
        numbers = list(map(int, input().split()))
        sudoku.append(numbers)

    result = 1

    for i in range(9):
        row_set= []
        col_set = []
        for j in range(9):
            row_set.append(sudoku[i][j])
            col_set.append(sudoku[j][i])
        if len(set(row_set)) != 9 or len(set(col_set)) != 9:
            result = 0
            break
    
    for i in range(0,9,3):
        for j in range(0,9,3):
            square_set = []
            for x in range(i,i+3):
                for y in range(j, j+3):
                    square_set.append(sudoku[x][y])
            if len(set(square_set)) != 9:
                result = 0
                break

    print(f'#{tc} {result}')