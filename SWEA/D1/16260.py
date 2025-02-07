T = int(input())

for tc in range(1, T+1):
  counts = [[0]*10 for _ in range(10)]

  N = int(input())
  for n in range(N):
    area = list(map(int, input().split()))

    # 색칠 된 부분 + 1
    for i in range(area[0], area[2]+1):
      for j in range(area[1], area[3]+1):
        counts[i][j] += 1
  
  # 2인 개수 세기
  result = 0
  for i in range(10):
    for j in range(10):
      if counts[i][j] == 2:
        result += 1
  
  print(f'#{tc} {result}')
