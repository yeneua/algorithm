# 중간값 찾기

num = int(input())
scores = list(map(int, input().split()))

scores.sort()
index = num // 2
print(scores[index])