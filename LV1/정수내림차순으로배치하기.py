# LV1 - 정수 내림차순으로 배치하기 문제의 해답
def solution(n):
    return int("".join(sorted(list(str(n)), reverse=True)))