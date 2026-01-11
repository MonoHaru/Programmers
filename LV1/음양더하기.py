# LV1 - 음영 더하기 문제의 해답
def solution(absolutes, signs):
    return sum([a if s else -a for a, s in zip(absolutes, signs)])