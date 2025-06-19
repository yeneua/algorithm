N, M = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()

def solution(cnt, path, visited):
    if cnt == M:
        print(*path)
    
    for i in range(N):
        if visited[i]: continue
        
        visited[i] = 1
        solution(cnt+1, path+[lst[i]], visited)
        visited[i] = 0

solution(0, [], [0] * N)