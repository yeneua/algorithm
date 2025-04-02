S, E = map(int, input().split())
during_time = int(input())

S += during_time // 60
E += during_time % 60

if E >= 60:
    S += E // 60
    E %= 60
    
if S >= 24:
    S -= 24

print(S, E)
