T = int(input())

for _ in range(1, T+1):
    tc, N = input().split()
    inputs = list(input().split())

    counts = [0] * 10

    numbers = {'ZRO' : 0, 'ONE':1, 'TWO':2, 'THR':3, 'FOR':4, 'FIV':5, 'SIX':6, 'SVN':7, 'EGT':8, 'NIN':9} # 키값 딕셔너리 생성

    for num in inputs:
        counts[numbers[num]] += 1 # 개수 카운팅

    print(tc)
    for key in numbers.keys():
        for _ in range(counts[numbers[key]]): # 개수만큼 ZRO부터 출력
            print(key, end=' ')
    print()
