a, b, c = map(int, input().split())

dice = set((a,b,c))

prize = 0 

if len(dice) == 3:
    max_num = max(a,b,c)
    prize = max_num * 100
    print(prize)
    
if len(dice) ==  1:
    prize = 10000 + (a * 1000)
    print(prize)

if len(dice) == 2:
    
    if a==b and a != c:
        num = a
    
    if a == c and a != b:
        num = a
    
    if b==c and a != b:
        num = b

    prize = 1000 + (num * 100)
    print(prize)
