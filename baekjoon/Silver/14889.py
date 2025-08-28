def calculate_stats(players):
    start_score = link_score = 0
    for i in range(N):
        if players[i] == 0:
            continue
        for j in range(N):
            if players[j] == 0 or i == j:
                continue
            start_score += stats[i][j]
    
    for i in range(N):
        if players[i] == 1:
            continue
        for j in range(N):
            if players[j] == 1 or i == j:
                continue
            link_score += stats[i][j]
    return abs(start_score - link_score)

def solution(cnt, current, start):
    global result
    
    if cnt == N/2:
        diff = calculate_stats(current)
        result = min(result, diff)
        return
    
    for i in range(start, N):
        if current[i]:
            continue
        current[i] = 1
        solution(cnt+1, current, i+1)
        current[i] = 0
    

N = int(input())
stats = [list(map(int, input().split())) for _ in range(N)]
result = float('inf')

solution(1, [1] + [0]*(N-1), 1)
print(result)