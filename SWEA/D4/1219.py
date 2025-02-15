def create_adj_matrix(edges, N):
    adj_matrix = [[] for _ in range(99)]

    for i in range(0, N*2, 2):
        adj_matrix[edges[i]].append(edges[i+1])
    
    return adj_matrix

def check_route(adj_matrix):
    s = 0 # 시작점
    G = 99 # 도착점

    visited = [0] * 100 # 방문했는지 검사
    stack = []
    
    v = s # 현재 위치
    visited[v] = 1
    while True:
        for w in adj_matrix[v]: # 현재 위치 v에서 갈 수 있는 정점 w탐색
            if visited[w] == 0: # 방문한 적 없으면
                v = w # 이동
                if v == G:
                    return 1
                visited[v] = 1
                stack.append(v)
                break # 새로 바뀐 v에서 정점 w를 탐색하기 위해 
        else: # 방문한 적이 없는 정점이 없으면
            if stack: # 스택이 비어 있지 않으면
                v = stack.pop() # 스택 젤 위에 있는 요소(==가장 최근에 방문한 곳)로 되돌아감
            else:
                return 0 # 종료(경로를 찾지 못함)


for _ in range(1, 11):
    tc, N = map(int, input().split())
    edges = list(map(int, input().split()))
    adj_matrix = create_adj_matrix(edges, N)
    print(f'#{tc} {check_route(adj_matrix)}')