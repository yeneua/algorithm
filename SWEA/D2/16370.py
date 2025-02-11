# 첫 번째 풀이
T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()
 
    max_count = -1
 
    for find_txt in str1:
        count = 0
        for txt in str2:
            if find_txt == txt:
                count += 1
        if max_count < count:
            max_count = count
 
    print(f'#{tc} {max_count}')


# 두 번째 풀이(내장함수 사용)
T = int(input())
for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    count = []

    for find_txt in str1:
        count.append(str2.count(find_txt))

    print(f'#{tc} {max(count)}')
