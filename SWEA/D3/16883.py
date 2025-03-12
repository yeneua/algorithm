T = int(input())

for tc in range(1, T+1):
    N = int(input())
    numbers = [list(map(int, input().split())) for _ in range(N)]

    
    dr = [0,1] # 우하
    dc = [1,0]
    
    min_sum = float('inf')
    def find_min_sum(r,c,cur_sum): # 현재 좌표, 현재 합
        global min_sum
        
        if cur_sum > min_sum: # 끝까지 가기 전에 현재 합이 최소 합보다 크면 중단
            return
        
        if r == N-1 and c == N-1: # 마지막 좌표(오른쪽 아래)일 경우 끝 -> 최소값 비교
            min_sum = min(min_sum, cur_sum)  
            return
        
        for d in range(2): # 우,하 두가지 방향 검사
            nr = r+dr[d]
            nc = c+dc[d]
            if nr < N and nc < N: # 범위 내인 경우만
                new_sum = cur_sum + numbers[nr][nc] # 다음 재귀로 넘겨줄 새로운 합 계산
                find_min_sum(nr, nc, new_sum)
    
    find_min_sum(0,0,numbers[0][0]) # 시작좌표
    
    print(f'#{tc} {min_sum}')
