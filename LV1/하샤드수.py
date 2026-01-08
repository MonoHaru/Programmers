# LV1 - 하샤드 문제의 해답
def solution(x):
    return not(x % sum(map(int, str(x))))