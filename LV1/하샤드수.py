# LV1 - 하샤드 수 문제의 해답
def solution(x):
    return not(x % sum(map(int, str(x))))