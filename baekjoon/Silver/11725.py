import sys
sys.setrecursionlimit(10**5+1)

# 부모 -> 자식으로 내려가는 형태
def find_parent(node):
    for child in edges[node]: # 1. 자식 탐색
        if visited[child] != 0: # 2. 방문 체크
            continue
        visited[child] = node # 3. 부모 저장
        find_parent(child) # 4. 재귀 호출

N = int(input())

# 간선 정보 저장
edges = [[] for _ in range(N+1)]
for _ in range(N-1):
    start, end = map(int, input().split())
    edges[start].append(end)
    edges[end].append(start)

visited = [0] * (N+1) # 방문 처리 + 부모 노드 저장
find_parent(1)

for x in visited[2:]:
    print(x)

'''
BOJ 서버에서 재귀 호출 횟수가 파이썬 제한(1000번)을 넘으면 에러 발생
setrecursionlimit()으로 최대 재귀 깊이 변경
https://www.acmicpc.net/board/view/160914
'''
