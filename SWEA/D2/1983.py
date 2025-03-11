T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    
    scores = {}
    
    for i in range(N):
        middle, final, report = map(int, input().split())
        scores[i+1] = middle*0.35 + final*0.45 + report*0.2 # 학생 번호를 키 값으로 딕셔너리 저장
        
    sorted_scores = list(scores.values()) # 점수를 리스트로 만든 후
    sorted_scores.sort(reverse = True) # 내림차순 정렬
    rank = sorted_scores.index(scores[K])+1 # 찾을 학생 번호를 scores의 인덱스로 이용하여 점수를 가져오고, 그 점수를 내림차순 정렬된 리스트에서의 인덱스를 통해 등수를 구함

    if 1 <= rank <= N//10:
        result = 'A+'
    elif N//10+1 <= rank <= 2*(N//10):
        result = 'A0'
    elif 2*(N//10)+1 <= rank <= 3*(N//10):
        result = 'A-'
    elif 3*(N//10)+1 <= rank <= 4*(N//10):
        result = 'B+'
    elif 4*(N//10)+1 <= rank <= 5*(N//10):
        result = 'B0'
    elif 5*(N//10)+1 <= rank <= 6*(N//10):
        result = 'B-'
    elif 6*(N//10)+1 <= rank <= 7*(N//10):
        result = 'C+'
    elif 7*(N//10)+1 <= rank <= 8*(N//10):
        result = 'C0'
    elif 8*(N//10)+1 <= rank <= 9*(N//10):
        result = 'C-'
    elif 9*(N//10)+1 <= rank <= 10*(N//10):
        result = 'D0'

    
    print(f'#{tc} {result}')
