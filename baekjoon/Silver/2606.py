from collections import deque

N = int(input())
K = int(input())

network = [[] for _ in range(N+1)]
for i in range(K):
    s, e = map(int, input().split())
    network[s].append(e)
    network[e].append(s)

q = deque()
visited = [0] * (N+1)

v = 1
visited[v] = 1
q.append(v)

while q:
    v = q.popleft()
    for w in network[v]:
        if visited[w] == 0 :
            visited[w] = 1
            q.append(w)

result = visited.count(1) - 1 # 처음 컴퓨터 제외
print(result)


'''
bfs
1. queue
2. visited
'''
