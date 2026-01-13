# LV1 - 나누어 떨어지는 숫자 배열 문제의 해답
def solution(arr, divisor):
    return sorted([e for e in arr if not e % divisor]) or [-1]