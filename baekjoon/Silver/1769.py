num = input()

total = 0
cnt = 0

if len(num) >= 2: # 두 자리수 이상
    cnt += 1
    
    for i in range(len(num)):
        total += int(num[i])

        
    while total >= 10:
        cnt += 1
        num = str(total)
        total = 0
        for i in range(len(num)):
            total += int(num[i])

    if total % 3 == 0:
        answer = 'YES'
    else:
        answer = 'NO'

    print(cnt, '\n', answer, sep='')
    
else: # 한 자리수
    
    if int(num) % 3 == 0:
        print(0, '\n', 'YES', sep='')
    else:
        print(0, '\n', 'NO', sep='')