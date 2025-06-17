N, M = map(int, input().split())
num = [i for i in range(1, N+1)]

def solution(cnt, start, path):
    if cnt == M:
        return print(*path)
    
    for i in range(start, N):
        solution(cnt+1, i, path+[num[i]])

solution(0, 0, [])
