N = int(input())

if N == 1:
    print('0')
elif N < 3:
    print('1')
else:
    lst = [0] * (N+1)
    lst[1] = 0
    lst[2] = lst[3] = 1

    for i in range(4, N+1):
        temp = i
        if i % 3 == 0:
            temp = min(temp, lst[i // 3])
        if i % 2 == 0:
            temp = min(temp, lst[i // 2])
        temp = min(temp, lst[i - 1])
        
        lst[i] = 1 + temp

    print(lst[N])

# 3으로 나눴을 때, 2로 나눴을때, 1을 뺐을때
# 각각의 경우 중 최소 연산 횟수를 고름
# N이 1일 경우 연산 횟수는 0임!!!
