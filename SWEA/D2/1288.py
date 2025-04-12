T = int(input())
for tc in range(1, T+1):
    N = int(input())
    
    number_set = set()
    
    count = 0
    number = 0
    
    while True:
        number += N
        count += 1
        
        for num in str(number):
            number_set.add(int(num))
        
        if len(number_set) == 10:
            break
    
    print(f'#{tc} {number}')
