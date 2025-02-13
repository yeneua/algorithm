T = int(input())

for _ in range(T):
    scores = input()
    count = 0
    result = 0

    for i in range(len(scores)):
        if scores[i] == 'O':
            count += 1
            result += count*1
        else:
            count = 0
          
    print(result)
