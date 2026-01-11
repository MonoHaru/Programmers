# LV0 - 수 조작하기 2 문제의 해답
def solution(numLog):
    key = dict(zip([1, -1, 10, -10], ['w', 's', 'd', 'a']))
    return ''.join([key[numLog[i] - numLog[i - 1]] for i in range(1, len(numLog))])