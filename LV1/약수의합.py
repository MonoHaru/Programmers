# LV1 - 약수의 합 문제의 해답
def solution(n):
    return sum([i for i in range(1, n + 1) if n % i == 0])