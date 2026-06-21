# LV0 - 치킨 쿠폰 문제의 해답
def solution(chicken):
    answer = 0
    while chicken >= 10:
        quot, rema = divmod(chicken, 10)
        
        answer += quot
        chicken = quot + rema
        
    return answer

print(solution(100))   # 11
print(solution(1081))  # 120