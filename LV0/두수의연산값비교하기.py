# LV0 - 두 수의 연산값 비교하기 문제의 답
def solution(a, b):
    return max(int(str(a)+str(b)), 2*a*b)