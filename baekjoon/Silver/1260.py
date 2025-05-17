# N : 정점의 개수
# M : 간선의 개수
# V : 시작 노드번호
from collections import deque

N, M, V = map(int, input().split())
edges = [[] for _ in range(N+1)]

for _ in range(M):
    start, end = map(int, input().split())
    edges[start].append(end)
    edges[end].append(start)
    
for edge in edges:
    edge.sort(reverse=True)
    
stack = [V]
visited = []

while stack:
    v = stack.pop()
    
    if v not in visited:
        visited.append(v)

        for w in edges[v]:
            if w not in visited:
                stack.append(w)

for edge in edges:
    edge.sort() 

# 2. BFS
q = deque()
visited_bfs = []
q.append(V)
visited_bfs.append(V)

while q:
    v = q.popleft()

    for w in edges[v]:
        if w in visited_bfs:
            continue

        q.append(w)
        visited_bfs.append(w)

print(*visited)
print(*visited_bfs)
