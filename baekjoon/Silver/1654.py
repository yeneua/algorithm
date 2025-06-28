def is_possible(length):
    cnt = 0
    for cable in cables:
        cnt += cable // length
    
    return cnt >= N

def find_cable_length(cables):
    left = 1 # 길이 1부터 시작
    right = max(cables)
    answer = -1

    while left <= right:
        mid = (left + right) // 2 # 자를 길이
        
        # 1. N개보다 많으면 늘리기
        if is_possible(mid):
            left = mid + 1
            answer = mid
            
        # 2. N개보다 적으면 줄이기
        else:
            right = mid - 1

    return answer
    

K, N = map(int, input().split())
cables = []
for _ in range(K):
    cables.append(int(input()))
print(find_cable_length(cables))
