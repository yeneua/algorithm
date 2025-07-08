N = int(input())

colors = [[0] * 3 for _ in range(N)]
dp = [[0] * 3 for _ in range(N)]

for i in range(N):
    r, g, b = map(int, input().split())
    colors[i][0] = r
    colors[i][1] = g
    colors[i][2] = b
    
    if i == 0:
        dp[i][0] = r
        dp[i][1] = g
        dp[i][2] = b

for i in range(1, N):
    dp[i][0] = colors[i][0] + min(dp[i-1][1], dp[i-1][2])
    dp[i][1] = colors[i][1] + min(dp[i-1][0], dp[i-1][2])
    dp[i][2] = colors[i][2] + min(dp[i-1][0], dp[i-1][1])

print(min(dp[N-1]))

# 현재 칠할 집 색을 제외한 두개 색 중 이전 집까지 칠하는 비용이 적은거 고르기
# ex. k번째 집 R
# -> (k-1)을 B로 칠한 것 vs (k-1)을 G로 칠한 것
# -> 둘 중에 작은 값
