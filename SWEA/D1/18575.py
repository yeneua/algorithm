T = int(input())

for tc in range(1,T+1):
    N = int(input())
    ballons = [list(map(int, input().split())) for _ in range(N)]

    answer = 0
    row_sum_list = [0] * N
    col_sum_list = [0] * N
    sum_list = [[0] * N for _ in range(N)]

    # 행의 합
    for i in range(N):
        row_sum = 0
        for j in range(N):
            row_sum_list[i] += ballons[i][j]
    
    # 열의 합
    for j in range(N):
        col_sum = 0
        for i in range(N):
            col_sum_list[j] += ballons[i][j]
    
    # 각 행, 열의 합
    for i in range(N):
        for j in range(N):
            sum_list[i][j] += row_sum_list[i] + col_sum_list[j] - ballons[i][j]
    

    # 최대 최소 구하기
    max_sum = float('-inf')
    min_sum = float('inf')
    for i in range(N):
        for j in range(N):
            if max_sum < sum_list[i][j]:
                max_sum = sum_list[i][j]
            if min_sum > sum_list[i][j]:
                min_sum = sum_list[i][j]

    result = max_sum - min_sum
    print(f'#{tc} {result}')