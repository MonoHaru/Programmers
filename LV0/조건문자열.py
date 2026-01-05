# LV0 - 조건 문자열 문제의 해답
def solution(ineq, eq, n, m):
    return int(eval(str(n) + ineq + eq.replace('!', '') + str(m)))