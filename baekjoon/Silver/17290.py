N = 10
r,c = map(int, input().split())
waters = [list(input()) for _ in range(N)]

r -= 1 # 입력은 가장 윗행이 1번이기 때문에 -1해줌
c -= 1

rows = [0] * N # 폭탄이 지나가는 부분을 1로 표시
cols = [0] * N

for i in range(N):
    for j in range(N):
        if waters[i][j] == 'o':
            rows[i] = 1
            cols[j] = 1

position = [] # 갇히지 않는 좌표

for i in range(N):
    if rows[i]: # 1이면(== 폭탄이 지나가는 부분) 컨티뉴
        continue
    for j in range(N):
        if cols[j]:
            continue
        position.append(abs(i-r) + abs(j-c)) # 이동 횟수 계산

position.sort() # 오름차순 정렬로 최소 이동횟수 구함
print(position[0])N = 10
r,c = map(int, input().split())
waters = [list(input()) for _ in range(N)]

r -= 1 # 입력은 가장 윗행이 1번이기 때문에 -1해줌
c -= 1

rows = [0] * N # 폭탄이 지나가는 부분을 1로 표시
cols = [0] * N

for i in range(N):
    for j in range(N):
        if waters[i][j] == 'o':
            rows[i] = 1
            cols[j] = 1

position = [] # 갇히지 않는 좌표

for i in range(N):
    if rows[i]: # 1이면(== 폭탄이 지나가는 부분) 컨티뉴
        continue
    for j in range(N):
        if cols[j]:
            continue
        position.append(abs(i-r) + abs(j-c)) # 이동 횟수 계산

position.sort() # 오름차순 정렬로 최소 이동횟수 구함
print(position[0])
