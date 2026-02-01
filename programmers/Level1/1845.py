from collections import Counter

def solution(nums):
    answer = 0
    
    animals = len(nums)//2
    counts = Counter(nums)
    
    if len(counts) >= animals:
        answer = animals
    else:
        answer = len(counts)

    return answer

'''
1. nums를 Counter 객체로 만든다
2-1. Counter 객체 길이가 N//2 이상이면 답은 N//2
2-2. Counter 객체 길이가 N//2 미만이면 답은 Counter 객체 길이
'''
