N, M = map(int, input().split())
num = [i for i in range(1,N+1)]

def solve(cnt, path, visited):
    if cnt == M:
        return print(*path)
    
    for i in range(N):
        if visited[i]: continue
        visited[i] = 1
        solve(cnt+1, path + [num[i]], visited)
        visited[i] = 0

solve(0,[],[0]*N)
