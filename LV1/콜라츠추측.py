# LV1 - 콜라츠 추측 문제의 해답
def solution(num):
    if num == 1:
        return 0
    
    cnt = 0
    while cnt < 500:
        if num % 2:
            num = num * 3 + 1
        else:
            num /= 2
        cnt += 1
        
        if num == 1:
            return cnt
    
    return -1