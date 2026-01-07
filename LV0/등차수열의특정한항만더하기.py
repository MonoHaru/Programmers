# LV0 - 등차수열의 특정한 항만 더하기 문제의 해답
def solution(a, d, included):
    return sum(a + (d * i) for i, j in enumerate(included) if j)