C, R = map(int, input().split())
K = int(input())

dr = [1,0,-1,0] # 하 우 상 좌
dc = [0,1,0,-1]

seats = [[0] * C for _ in range(R)]

answer = 0

r = c = 0
count = 1

seats[r][c] = count
if K == 1:
    answer = (r, c)
count += 1

for d in range(4 * R//2): # R개의 행이 있으면 R//2개의 사각형이 생김 -> d가 0~3이 한바퀴니까 4 * (R//2)번 반복
    while True:
        nr = r + dr[(d%4)]
        nc = c + dc[(d%4)]
        if nr < 0 or nr >= R or nc < 0 or nc >= C or seats[nr][nc] != 0:
            break
        else:
            seats[nr][nc] = count
            if count == K:
                answer = (nc, nr) # (x, y) 좌표 출력
            count += 1
            r, c = nr, nc

if answer == 0:
    print(answer)
else:
    print(answer[0]+1, answer[1]+1)
