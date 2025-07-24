import math

N = int(input())
lst = list(map(int, input().split()))
B, C = map(int, input().split())

answer = 0
for i in range(N):
    if lst[i] < B:
        answer += 1
        lst[i] = 0
        
    if lst[i] >= B:
        answer += 1
        lst[i] -= B
    
    if lst[i] > 0:
        answer += math.ceil(lst[i]/C)

print(answer)
