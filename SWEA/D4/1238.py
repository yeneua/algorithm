from collections import deque

for tc in range(1,11):
    N, S = map(int, input().split())
    edges = list(map(int, input().split()))
    
    contact_list=[[]  for _ in range(101)]
    for i in range(N//2):
        s, e = edges[i*2], edges[i*2+1]
        contact_list[s].append(e)
    
    q = deque()
    contacted = [0] * 101 # 연락인원 최대 100명

    v = S # v : 현재 노드
    q.append(v)
    contacted[v] = 1

    while q:
        v = q.popleft()

        for w in contact_list[v]:
            if contacted[w] == 0:
                q.append(w)
                contacted[w] = contacted[v] + 1 # 몇번째에 연락을 받았는지
    
    max_count = 0
    max_number = 0
    
    for i in range(101):
        if max_count <= contacted[i]: # 가장 번호가 큰 사람 -> 등호
            max_count = contacted[i]
            max_number = i

    print(f'#{tc} {max_number}')

'''
필요한거
1. 큐
2. 방문했는지

진행과정
1. 시작 노드
2. 시작노드방문 체크
3. 큐에 append
3. while 시작
    1. popleft()
    2. 갈수있는정점탐색
        1. visited = 0
    3. 방문체크
    4. append
    5. 계속 탐색
    6. 갈수있는 정점 없으면
    7. popleft

    8. queue가 비면
    9. 끝
4. 가장 나중에 연락받은사람
5. 그중에 최대
'''
