# 2026 카카오그룹 신입크루 공채 1차 코딩테스트

def solution(message, spoiler_ranges):
    answer = 0

    words = list(message.split()) # 단어
    index = [] # 단어 인덱스 범위
    for i in range(len(message)):
        if i != 0 and message[i-1] == ' ':
            start = i
        
        if i == 0:
            start = i

        for j in range(i, len(message)):
            if j != len(message)-1 and message[j+1] == ' ':
                index.append((start, j))
            if j == len(message-1):
                index.append((start,j))
            break

        is_spoiler = [0] * len(index) # 단어 스포방지 문자 여부

        for spoiler in spoiler_ranges:
            start = spoiler[0]
            end = spoiler[1]

            for k in range(len(index)):
                if index[k][0] <= start and index[k][1] >= start:
                    is_spoiler[k] = 1

                
                if index[k][0] >= start and index[k][1] <= end:
                    is_spoiler[k]=1

                if index[k][0] >= start and index[k][0] <= end:
                    is_spoiler[k] = 1

        
        is_spoiler_words = []
        is_not_spoiler_words = []

        for i in range(len(is_spoiler)):
            if is_spoiler[i] == 0:
                is_not_spoiler_words.append(words[i])
            else:
                is_spoiler_words.append(words[i])
        
        for i in range(len(is_spoiler_words)):
            if is_not_spoiler_words.count(is_spoiler_words[i]) != 0:
                continue
            if is_spoiler_words.count(is_spoiler_words[i]) == 1:
                answer += 1
            else:
                if is_spoiler_words.index(is_spoiler_words[i]) == i:
                    answer += 1


'''
입력

message
"here is muzi here is a secret message"
spoiler_ranges
[[0,3],[23,28]]
result 
1

message
"my phone number is 01012345678 and may i have your phone number"
spoiler_ranges
[[5,5],[25,28],[34,40],[53,59]]
result
4
'''