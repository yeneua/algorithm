T = int(input())
for tc in range(1, T+1):
    position = 0
    cur_speed = 0
  
    N = int(input())
    for _ in range(N):
        speed = input()
        
        if len(speed) == 1: # 속도 유지
            position += cur_speed
        else:
            speed, distance = map(int, speed.split())
            if speed == 1: # 가속
                cur_speed += distance # 현재 속도 + 가속도
                position += cur_speed # 현재 위치는 가속도만큼 더해짐
            elif speed == 2: # 감속
                if cur_speed <= distance: # 현재 속도 보다 같거나 더 많이 감속할 경우
                    cur_speed = 0
                else:
                    cur_speed -= distance
                    position += cur_speed
        
    print(f'#{tc} {position}')
