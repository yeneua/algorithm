for tc in range(1,11):

    T = int(input())
    numbers = []
    
    for i in range(100):
        temp_numbers = list(map(int, input().split()))
        numbers.append(temp_numbers)

    max_row_sum = 0
    max_col_sum = 0
    max_across_sum = 0
    max_across_reverse_sum = 0
    result = []
    answer = 0    
    
    for i in range(len(numbers)):
        row_sum = 0
        col_sum = 0
        for j in range(len(numbers)):
            row_sum += numbers[i][j] # 행 순회 - 행 최대값
            col_sum += numbers[j][i] # 열 순회 - 열 최대값
        if max_row_sum < row_sum:
            max_row_sum = row_sum       
        if max_col_sum < col_sum:
            max_col_sum = col_sum
   
    for i in range(len(numbers)):
        max_across_sum += numbers[i][i]  # 대각선합 - 왼쪽상단~오른쪽하단
        max_across_reverse_sum += numbers[i][len(numbers)-1-i] # 대각선합 - 오른쪽상단~왼쪽하단

    result.extend([max_row_sum, max_col_sum, max_across_sum, max_across_reverse_sum])

    for num in result:
        if answer < num:
            answer = num
    print(f'#{tc} {answer}')
