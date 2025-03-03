def battle(left,right):
    if cards[left] == cards[right]:
        return left
    elif cards[left] == 1:
        if cards[right] == 2:
            return right
        else:
            return left
    elif cards[left] == 2:
        if cards[right] == 1:
            return left
        else:
            return right
    elif cards[left] == 3:
        if cards[right] == 1 :
            return right
        else:
            return left
   
def tournament(i, j):
    if i==j: # 쪼갤수 없을 때까지 쪼개기
        return i # 시작과 끝이 같으면 == 사람 1명
    else:
        left = tournament(i, (i+j)//2)
        right = tournament((i+j)//2 + 1, j)
        return battle(left, right)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cards =  [0] + list(map(int, input().split()))
    print(f'#{tc} {tournament(1,N)}')
