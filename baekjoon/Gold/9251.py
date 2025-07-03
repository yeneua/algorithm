str1 = list(input())
str2 = list(input())

dp = [[0] * (len(str2)+1)  for _ in range(len(str1)+1)]

for i in range(1, len(str1)+1):
    for j in range(1, len(str2)+1):
        if str1[i-1] == str2[j-1]: # 같은 문자열일 경우
            dp[i][j] = dp[i-1][j-1] + 1 # 직전 결과 + 1
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])

answer = 0
for row in dp:
    answer = max(answer, max(row))
print(answer)
