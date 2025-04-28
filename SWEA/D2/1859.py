T = int(input())
 
for tc in range(1, T+1):
    N = int(input())
    price = list(map(int, input().split()))
     
    profit = 0
    max_profit = price[-1]
     
    for i in range(N-2, -1, -1):
        if max_profit > price[i]:
            profit += max_profit - price[i]
        else:
            max_profit = price[i]
 
    print(f'#{tc} {profit}')
