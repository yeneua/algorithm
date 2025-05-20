N = int(input())
score = list(map(int, input().split()))

total = 0
max_score = max(score)

for i in range(N):
    total += score[i]/max_score*100

print(total/N)
