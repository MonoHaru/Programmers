# LV2 - 최댓값과 최솟값 문제의 해답
def solution(s):
    s = list(map(int, s.split(' ')))
    return str(min(s)) + ' ' + str(max(s))