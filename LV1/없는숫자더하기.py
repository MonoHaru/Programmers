# LV1 - 없는 숫자 더하기 문제의 해답
def solution(numbers):
    return sum([i for i in range(0, 10) if i not in numbers])