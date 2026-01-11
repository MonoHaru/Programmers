# LV0 - 수 조작하기 1 문제의 해답
def solution(n, control):
    key = dict(zip(['w', 's', 'd', 'a'], [1, -1, 10, -10]))
    return n + sum([key[c] for c in control])