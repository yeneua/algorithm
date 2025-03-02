T = int(input())

for tc in range(1,T+1):

    N = int(input())
    numbers = [list(map(int, input().split())) for _ in range(N)]

    min_sum = float('inf')

    def find_min_sum(row, cur_sum, visited):
        global min_sum

        if cur_sum > min_sum: # 현재 합이 최소 합보다 커지면 중단
            return
        
        if row == N: # 마지막 행까지 다 돌았으면 최소합 비교 및 갱신
            min_sum = min(min_sum, cur_sum)
            return

        for j in range(N): # 한 행에서 0~N-1 열 인덱스 확인
            if visited[j]: # 방문한 행이면 넘어감
                continue
            new_sum = cur_sum + numbers[row][j]  # 함 더하기
            new_visited = visited[:] # 다음 행에 넘겨줄 visited 배열
            new_visited[j] = 1 # 다음 행에 넘겨줄 visited 배열 -> 현재 행에서 방문한 열번호를 1로 표시해줌
            find_min_sum(row+1, new_sum, new_visited) # 다음 행 재귀

    visited =[0] * N
    find_min_sum(0,0,visited)

    print(f'#{tc} {min_sum}')
