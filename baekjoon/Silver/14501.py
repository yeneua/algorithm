N = int(input())
days = [0] * N
cost = [0] * N

for i in range(N):
    a, b = map(int, input().split())
    days[i] = a
    cost[i] = b

dp = [0] * (N+1)

for i in range(N-1, -1, -1):
    if days[i] + i <= N: # 일자를 넘기지 않으면
        dp[i] = max(dp[i+1], cost[i] + dp[i+days[i]]) # 상담하는 것과 안하는 것 중 max 비교
    else: # 넘기면
        dp[i] = dp[i+1]

print(dp[0])

'''
dp[i] = max(dp[i+1], cost[i] + dp[i+days[i]])

1) cost[i] : 현재 일자 상담 비용
2) dp[i + days[i]]
만약 현재 지금 4일째고, days[4] = 2라고 가정하면
dp[4 + days[4]] = dp[6] 6일째 상담 비용을 나타냄
days[4] = 2로 5일째는 상담 못하니까!
'''