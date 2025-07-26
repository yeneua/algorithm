dr = [0,1] # 우하
dc = [1,0]

graph = [[0] * 100 for _ in range(100)]

for _ in range(4):
    left_c, left_r, right_c, right_r = map(int, input().split())
    
    for i in range(right_r - left_r):
        for j in range(right_c - left_c):
            nr = left_r + dr[1]*i
            nc = left_c + dc[0]*j
            graph[nr][nc] += 1

answer = 0
for row in graph:
    answer += row.count(0)

print(10000-answer)   
    
