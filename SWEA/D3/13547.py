T = int(input())

for tc in range(1, T+1):
    game = list(input())
    
    result = 'YES'
    
    if game.count('x') >= 8:
        result = 'NO' # 점심을 면제 받을 '가능성' -> 8번 이상 진 경우 가능성 없음
    
    print(f'#{tc} {result}')
