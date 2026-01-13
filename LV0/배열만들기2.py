# LV0 - 배열 만들기 2 문제의 해답
def solution(l, r):
    answer = []
    for i in range(l, r + 1):
        num = set(str(i)) - set(['0', '5'])
        if not num:
            answer.append(i)
    return [-1] if not answer else answer