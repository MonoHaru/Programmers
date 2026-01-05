# LV1 - x만큼 간격이 있는 n개의 숫자 문제의 해답
def solution(x, n):
    return [x * (i + 1) for i in range(n)]