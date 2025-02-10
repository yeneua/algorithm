T = int(input())

for tc in range(1 ,T+1):
    N, page_A, page_B = map(int, input().split())

    answer = {'A': 'A', 'B':'B', 'tie':0}
    result = ''

    def binary_search(page):
        count = 0
        start = 1
        end = N

        while start <= end:
            middle = int((start + end) / 2)
            if middle == page:
                return count
            if middle < page:
                count += 1
                start = middle # start를 middle로
            if middle > page:
                count += 1
                end = middle # end를 middle로

    count_A = binary_search(page_A)
    count_B = binary_search(page_B)

    if count_A < count_B:
        result = 'A'
    elif count_A > count_B:
        result = 'B'
    else:
        result = 'tie'

    print(f'#{tc} {answer[result]}')
