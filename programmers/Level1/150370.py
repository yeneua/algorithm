# 2023 KAKAO BLIND RECRUITMENT - 개인정보 수집 유효기간
def solution(today_input, terms_input, privacies_input):
    answer = []
    
    # input
    today_y, today_m, today_d = map(int, today_input.split('.'))
    
    terms = {}
    for term in terms_input:
        type, duration = term.split()
        terms[type] = int(duration)

    privacies = []
    for privacy in privacies_input:
        duration, type = privacy.split()
        y, m, d = map(int, duration.split('.'))
        privacies.append([y,m,d,type])

   # 날짜 계산
    for i in range(len(privacies)):
        y, m, d = privacies[i][0], privacies[i][1], privacies[i][2]
        duration = terms[privacies[i][-1]]
        
        expired_y = y
        expired_m = m
        expired_d = d
        
        expired_m = m + duration
        if expired_m > 12:
            if expired_m % 12 == 0: # 12의 배수가 됐을때
                expired_y += (expired_m // 12) - 1
                expired_m = 12
            else:
                expired_y += expired_m // 12 # 유효 기간 범위 체크 (1 <= 유효기간 <= 100)
                expired_m = expired_m % 12
        
        expired_d = d - 1
        
        if expired_d <= 0: # 1일에 시작할 경우 -> 만료 일자는 28일
            expired_d = 28
            expired_m -= 1
        
        if m == 12 and duration == 1: # 12.01 시작 & 유효 기간 1달인 경우
            expired_y = y
            expired_m = m
            expired_d = 28

        # 오늘 날짜랑 비교
        if expired_y < today_y:
            answer.append(i+1)
            continue
            
        if expired_y == today_y and expired_m < today_m:
            answer.append(i+1)
            continue
        
        if expired_y == today_y and expired_m == today_m and expired_d < today_d:
            answer.append(i+1)
            continue
    
    print(answer)
    
    return answer

'''
1. input
1) 오늘 날짜 int로 변경
2) terms 딕셔너리로
3) privacies: 숫자는 int로

2. 날짜 계산
1) month + 기간(duration)
1-1) 12의 배수가 될 경우
1-2) 12의 배수가 아닐 경우

2) 일자 -= 1
2-1) 1일에 시작할 경우 -1을 하면 0이 되니 28로 지정
2-2) 12.01 시작 & 유효 기간이 1달인 경우 예외 케이스로 따로 계산

3. 오늘 날짜랑 비교
'''