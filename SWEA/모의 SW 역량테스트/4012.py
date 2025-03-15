T = int(input())
for tc in range(1, T+1):
    N = int(input())
    synergy = [list(map(int, input().split())) for _ in range(N)]
    min_diff = float('inf')
    
    def calculate_synergy(arr): # N/2개 중에서 2개씩 뽑아 synergy 계산하는 함수
        
        def subset(start, cur_subset):
            
            if len(cur_subset) == 2:
                result.append(synergy[cur_subset[0]][cur_subset[1]])
                result.append(synergy[cur_subset[1]][cur_subset[0]])
                return
        
            for i in range(start, N//2):
                subset(i+1, cur_subset+[arr[i]])
        
        result = []
        subset(0,[])
        return sum(result) # ex. N=6일때 [0,1,2] 조합이 내는 시너지 리턴
    
    def get_combination(count): # N개 중 N/2개 조합 뽑는 함수
        
        def subset(start, cur_subset):
            
            if len(cur_subset) == count:
                result.append(cur_subset)
                return
            
            for i in range(start, N):
                subset(i+1, cur_subset+[i])    
                    
        result = []
        subset(0, [])
        return result # 조합 결과를 리턴
    
    combinations = get_combination(N//2) # N/2 개 조합
    
    R = len(combinations)
    for i in range(R//2):
        food_A = calculate_synergy(combinations[i]) # 조합을 하나 선택하면
        food_B = calculate_synergy(combinations[R-1-i]) # 나머지 조합은 자동으로! -> 재귀로 만든 조합이라서 0번째랑 N번째는 세트임
        
        diff = abs(food_A - food_B)
        if min_diff > diff:
            min_diff = diff
        
    print(f'#{tc} {min_diff}')

'''
1. N개 중에서 N/2개 조합을 뽑는다.
    - get_combination 함수
    - N개의 음식이니까 0~N-1 인덱스로 뽑음
2. N/2개에서 2개씩 조합하여 시너지를 계산한다
    - for문, calculate_synergy 함수
    - 1번에서 얻은 조합들을 for문 돌림
    - calculate_synergy 함수로 N/2개에서 2개를 뽑아 계산한 시너지 반환
    - for문 내에서 시너지 차이 계산하고 최소값 갱신
    - ex. N=6일때, [0,1,2]를 선택하면 나머지 [3,4,5] 조합이 선택됨
    - 재귀로 조합을 구했기 때문에 0번째-19번째, 1번째-18번째는 세트임 -> i, R-1-i
3. 시너지 차이의 최소값을 찾는다
'''
