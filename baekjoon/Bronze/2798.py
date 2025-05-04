N, M = map(int, input().split())
cards = list(map(int, input().split()))

answer = 0

def get_combi(start, cur): # 3개 조합 뽑기
    global answer
    
    if sum(cur) > M:
        return
    
    if len(cur) == 3 and sum(cur) <= M:
        answer = max(answer, sum(cur))
        return
    
    for i in range(start, N):
        get_combi(i+1, cur+[cards[i]])
        
get_combi(0, [])
print(answer)
