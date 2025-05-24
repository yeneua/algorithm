while True:
    try:
        a, b = map(int, input().split())
        print(a+b)
    except EOFError: # 입력의 마지막
        break
