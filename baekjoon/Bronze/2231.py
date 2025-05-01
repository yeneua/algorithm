N = int(input())
answer = 0

for i in range(N):
    idx = i
    temp = i
    
    while idx:
        temp += idx % 10
        idx = idx // 10
    
    if temp == N:
        answer = i
        break
        
print(answer)
