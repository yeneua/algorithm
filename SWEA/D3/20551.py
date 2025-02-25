def check_box_full(A,B,C): # 상자 안에 사탕이 1개 이상인지 확인
    if A < 1 or B < 1 or C < 1:
        return -1
    else:
        pass

def check_increase(A,B,C): # 이미 조건이 만족되었는지 검사
    if A < B < C:
        return True

def count_candy(A,B,C): # 몇개 먹을건지
    count = 0
    while True:
        if B < C:
            break
        B -= 1
        count += 1
    while True:
        if A < B:
            break
        A -= 1
        count += 1
    if check_box_full(A,B,C) == -1: # 증가하는 경우를 만들었는데 + 그때 상자 안에 사탕이 1개 이상인지
        return -1
    
    return count


T = int(input())
for tc in range(1,T+1):
    A, B, C = map(int,input().split())

    if check_box_full(A,B,C) == -1:
        answer = -1
    else:
        if check_increase(A,B,C):
            answer = 0
        else:
            count = count_candy(A,B,C)
            if check_box_full(A,B,C) == -1:
                answer = -1
            else:
                answer =  count
    print(f'#{tc} {answer}')

    '''
    main 로직
    1. 1개 이상이 아니면 -1
    2. 한개 이상일때
        a. 이미 조건이 만족했는지 검사(A<B<C)
        b. 아니라면
            i. 몇개 먹어야하는지 카운트
            ii. 사탕 먹은 후, 각 상자에 1개 이상인지 확인     
    '''
