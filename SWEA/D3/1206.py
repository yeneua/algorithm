for test_case in range(10):
    N = int(input())
    heights = list(map(int, input().split()))

    count = 0

    for i in range(2, N-2):
        buildings = heights[i-2:i+3]
        buildings.pop(2)

        if max(buildings) < heights[i]:
            count += (heights[i] - max(buildings))

    print(f'#{test_case+1} {count}')
