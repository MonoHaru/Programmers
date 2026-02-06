# LV1 - 크기가 작은 부분 문자열 문제의 해답
def solution(t, p):
    """
    :param t: str
    :param p: str
    :return: int
    """
    cnt = 0
    for i in range(len(t)-len(p)+1):
        if int(t[i:i+len(p)]) <= int(p):
            cnt += 1         
    return cnt

print(solution("3141592", "271"))  # 2
print(solution("500220839878", "7"))  # 8
print(solution("10203", "15"))  # 3