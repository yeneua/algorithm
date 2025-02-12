N = int(input())
switch = list(map(int, input().split()))
student = int(input())

for _ in range(student):
    gender, number = map(int, input().split())
    
    if gender == 1:
        for k in range(number-1, N, number):
            switch[k] = int(not switch[k])

    if gender == 2:
        switch[number-1] = int(not switch[number-1])
        k = 0
        while True:
            if number-1-k < 0 or number-1+k >=N: # 리스트 범위 내에서만
                break
            if switch[number-1-k] == switch[number-1+k]: # 같으면 스위치 바꾸기
                switch[number-1-k] = int(not switch[number-1-k])
                switch[number-1+k] = int(not switch[number-1+k])
            else: # 다를 경우 break
                break
            k += 1

for i in range(0, len(switch),10):
    print(*switch[i:i+10])