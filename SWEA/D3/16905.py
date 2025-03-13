def is_run(arr):
    for i in range(0, len(arr) - 2):
        if arr[i] + 2 == arr[i + 1] + 1 == arr[i + 2]:
            return 1
    for i in range(0,len(arr)-3):
        if len(set((arr[i],arr[i+1],arr[i+2],arr[i+3]))) == 3: # 예) 1,2,2,3 경우 고려
            if arr[i] + 2 == arr[i+1]+1 == arr[i+3]:
                return 1
    else:
        return 0

def is_triplet(arr):
    for i in range(0, len(arr) - 2):
        if arr[i] == arr[i + 1] == arr[i + 2]:
            return 1
    else:
        return 0

T = int(input())

for tc in range(1, T+1):
    cards = list(map(int, input().split()))

    player1 = []
    player2 = []

    player1_count = 0
    player2_count = 0

    result = 0

    for i in range(12):
        if i % 2 == 0: # input 데이터를 player1,2로 나눔
            player1.append(cards[i])
            player1.sort()
            if len(player1) >= 3: # 길이가 3이상이면 run, triplet 검사
                if is_run(player1) or is_triplet(player1):
                    result = 1
                    break

        else:
            player2.append(cards[i])
            player2.sort()
            if len(player2) >= 3:
                if is_run(player2) or is_triplet(player2):
                    result = 2
                    break

    print(f'#{tc} {result}')
