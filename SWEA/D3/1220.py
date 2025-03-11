for tc in range(1,11):
    N = int(input())
    magnetics = [list(map(int, input().split())) for _ in range(N)] # 1 : N극(아래로 == S극 쪽으로), 2 : S극(위로)
    dr = [-1,1] # 상하 -> 행번호만 변함

    for i in range(N):
        for j in range(N):
            if magnetics[i][j] == 1:
                nr = i + dr[1]
                if nr == N:
                    magnetics[i][j] = 0
                elif magnetics[nr][j] == 0:
                    magnetics[i][j], magnetics[nr][j] = 0,1
                elif magnetics[nr][j] == 1:
                    pass
            elif magnetics[i][j] == 2:
                nr = i + dr[0]
                if nr == -1:
                    magnetics[i][j] = 0
                elif magnetics[nr][j] == 0:
                    magnetics[i][j], magnetics[nr][j] = 0, 2
                elif magnetics[nr][j] == 2:
                    pass

    result = 0
    for i in range(N-1):
        for j in range(N):
            if magnetics[i][j] == 1 and magnetics[i+1][j] == 2:
                result += 1

    print(f'#{tc} {result}')
