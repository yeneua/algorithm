T = int(input())

for tc in range(1, T + 1):
    board = [list(input().split()) for _ in range(4)]

    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    result = set() # set 이용 -> 수를 저장, 중복 제거

    def attach_numbers(numbers, r, c):
        if len(numbers) == 7:
            result.add(numbers)
            return

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]

            if 0 <= nr < 4 and 0 <= nc < 4:
                attach_numbers(numbers + board[nr][nc], nr, nc) # 다움 숫자(문자열)를 추가하면서 재귀 호출

    for i in range(4):
        for j in range(4):
            attach_numbers(board[i][j], i, j)

    print(f'#{tc} {len(result)}')

'''
리스트 not in 방식 -> O(n)이기 때문에 시간 초과남
set 쓰면 O(1)
'''
