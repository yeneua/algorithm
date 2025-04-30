while True:
    lengths = list(map(int, input().split()))
    if lengths.count(0) == 3:
        break
      
    lengths.sort()

    result = 'wrong'

    if lengths[0] ** 2 + lengths[1] ** 2 == lengths[2] **2:
        result = 'right'

    print(result)
