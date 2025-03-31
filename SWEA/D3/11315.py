def is_checked():
    
    result = 'NO'
    
    # 1. 가로 검사
    for i in range(N):
        count = 0
        for j in range(N):
            if board[i][j] == 'o':
                count += 1
                if count >= 5:
                    result = 'YES'
                    return result
            else:
                count = 0
    
    # 2. 세로 검사
    for j in range(N):
        count = 0
        for i in range(N):
            if board[i][j] == 'o':
                count += 1
                if count >= 5:
                    result = 'YES'
                    return result
            else:
                count = 0
    for i in range(N):
        col = [col[i] for col in board]
        combined = ''.join(col)
        splitted = combined.split('.')
        if 'ooooo' in splitted:
                result = 'YES'
                return result

    
    # 3. 대각선 검사
    # 1) 좌상-우하
    for i in range(N-4):
        for j in range(N-4):
            combined = ''
            for k in range(5):
                combined += board[i+k][j+k]
            if combined == 'ooooo':
                result = 'YES'
                return result

    
    # 2) 우상 - 좌하
    for i in range(N-4):
        for j in range(4,N):
            combined = ''
            for k in range(5):
                combined += board[i+k][j-k]
            if combined == 'ooooo':
                result = 'YES'
                return result

    return result
    

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    board = [input() for _ in range(N)]    
    print(f'#{tc} {is_checked()}')
