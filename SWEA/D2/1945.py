T = int(input())

for tc in range(1, T+1):
    number = int(input())
    result = []
    count = 0

    primes = [2,3,5,7,11]

    for prime in primes:
        count = 0
        while True:
            if number % prime:
                break
            else:
                number /= prime
                count += 1
    
        result.append(count)
    
    print(f'#{tc}', end=' ')
    for counts in result:
        print(counts, end = ' ')
    print()