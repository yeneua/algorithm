N, M = map(int, input().split())

def solution(cnt, path):
    if cnt == M:
        return print(*path) # return으로 종료시키기
    
    for i in range(1,N+1):
        solution(cnt+1, path+[i])

solution(0, [])