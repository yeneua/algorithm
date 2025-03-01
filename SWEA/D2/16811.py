T = int(input())

for tc in range(1,T+1):
    N = int(input())
    carrots = sorted(list(map(int, input().split())))
    carrots_count = []

    count = 1 # 당근 개수 세기
    for i in range(N-1):
        if carrots[i] == carrots[i+1]:
            count += 1
        else:
            carrots_count.append(count)
            count = 1
    carrots_count.append(count)

    answer = float('inf')

    for k in range(len(carrots_count)): # 당근 나누기
        for l in range(k+1, len(carrots_count)):
            small = carrots_count[:k]
            medium = carrots_count[k:l]
            large = carrots_count[l:]

            if 0 < sum(small) <= N/2 and 0 < sum(medium) <= N/2 and 0 < sum(large) <= N/2:
                size_len = [sum(small), sum(medium), sum(large)]
                temp = max(size_len)- min(size_len)
                answer = min(temp, answer)

    if answer == float('inf'):
        answer = -1
               
    print(f'#{tc} {answer}')
