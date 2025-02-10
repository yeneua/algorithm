for tc in range(1,11):
    T = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    
    dx = [-1, 0, 0] # 상 좌 우
    dy = [0, -1, 1] # 상 좌 우

    r = 99
    c = ladder[99].index(2)
    d = 0

    while True:
        if d == 0: # ↑
            r += dx[d]
            c += dy[d]
            if c >= 1 and ladder[r+dx[1]][c+dy[1]] == 1:  # ← 방향에 1이 있는지 확인
                d = 1
            if c <= 98 and ladder[r+dx[2]][c+dy[2]] == 1: # → 방향에 1이 있는지 확인
                d = 2
        
        if d==1 or d==2: # ← or →
            r += dx[d]
            c += dy[d]
            if ladder[r+dx[0]][c+dy[0]] == 1: # ↑ 방향에 1이 있는지 확인
                d = 0
        if r == 0: break
        
    print(f'#{tc} {c}')