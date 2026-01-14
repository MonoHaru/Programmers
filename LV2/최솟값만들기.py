# LV2 - 최솟값 만들기 문제의 해답
def solution(A, B):
    return sum([a * b for a, b in zip(sorted(A), sorted(B, reverse=True))])