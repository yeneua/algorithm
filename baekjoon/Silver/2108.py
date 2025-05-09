N = int(input())
lst = [0] * N
for i in range(N):
    lst[i] = int(input())
lst.sort()

if N > 1:
    avg = round(sum(lst)/N)
    median = lst[N//2]
    lst_range = lst[-1] - lst[0]
    
    mode = 0

    idx = lst[0]
    count = 0
    mode_lst = [] # 연속된 숫자 개수 (개수, 숫자)
    for i in range(N):
        if lst[i] == idx:
            count += 1
            if i == N-1:
                mode_lst.append((count, lst[i]))
        else:
            mode_lst.append((count, idx))
            idx = lst[i]
            count = 1
            if i== N-1:
                mode_lst.append((count, lst[i]))
    
    mode_lst.sort(key=lambda x:(-x[0], x[1])) # 1. count 내림차순, 2. 숫자 오름차순
    
    if len(mode_lst) >= 2:
        if mode_lst[0][0] == mode_lst[1][0]:
            mode = mode_lst[1][1]
        else:
            mode = mode_lst[0][1]
    else:
        mode = mode_lst[0][1]

else:
    avg = lst[0]
    median = lst[0]
    mode = lst[0]
    lst_range = 0

print(avg)
print(median)
print(mode)
print(lst_range)
