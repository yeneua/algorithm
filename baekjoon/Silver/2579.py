N = int(input())

stairs = [0] * N
score = [0] * N

for i in range(N):
    stairs[i] = int(input())

if N >= 1:
    score[0] = stairs[0]
if N >= 2:
    score[1] = stairs[0] + stairs[1]
if N >= 3:
    score[2] = max(stairs[0] + stairs[2], stairs[1] + stairs[2])
if N > 3:
    for k in range(3, N):
        score[k] = max(score[k-2], stairs[k-1] + score[k-3]) + stairs[k]

print(score[N-1])

# n번째 계단을 밟는 경우
# 1) n-3 -> n-1 -> n
# 2) n-2 -> n
