N, M = map(int, input().split())

def func(cnt, start, path, visited):
    if cnt == M:
        print(*path)
    
    for i in range(start, N+1): # 이전에 고른 숫자보다 같거나 큰 숫자만 고름(오름차순)
        if visited[i]: continue
        
        visited[i] = 1
        func(cnt+1, i, path+[i], visited)
        visited[i] = 0
        
func(0, 1, [], [0]*(N+1))
