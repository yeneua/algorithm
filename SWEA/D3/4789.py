T = int(input())
for tc in range(1,T+1):
    people = list(map(int, input()))
    
    answer = 0
    cur_people = 0
    
    for i in range(len(people)): # i(인덱스) : 기립 박수를 칠 수 있는 특정 사람 수
        if people[i] == 0:
            continue
        
        if i <= cur_people: # 조건 만족하면 현재 박수 치는 사람들 인원에 기립 박수 시작하는 사람 추가
            cur_people += people[i]
            
        else:
            add = i - cur_people # add : 추가되어야 하는 인원
            answer += add
            cur_people += add # 추가되는 만큼 현재 박수 치는 인원에 추가
            cur_people += people[i]
    
    print(f'#{tc} {answer}')
