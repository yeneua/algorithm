T = int(input())
 
for tc in range(1, T+1):
    N, B = map(int, input().split())
    heights = list(map(int, input().split()))
 
    min_diff = float('inf')
 
    for i in range(1<<N): # 2^N번 반복 == 부분집합의 개수
        subset = []
        number = i
        for j in range(N): 
            if number & 1: # 비트연산으로 부분집합 만들기
                subset.append(heights[j])
            number >>= 1
 
        if sum(subset) >= B:
            diff = sum(subset) - B
            if min_diff > diff:
                min_diff = diff
 
    print(f'#{tc} {min_diff}')
