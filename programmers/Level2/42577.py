def solution(phone_book):
    answer = True
    
    phone_book.sort()
    
    for idx, num in enumerate(phone_book):
        if idx == len(phone_book) - 1:
            continue
        
        if phone_book[idx+1].startswith(num):
            answer = False
            break
    
    return answer
