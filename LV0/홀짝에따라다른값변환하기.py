# LV0 - 홀짝에 따라 다른 값 반환하기 문제의 해답
def solution(n):
    if n % 2:
        return sum(range(1, n+1, 2))
    else:
        return sum([i**2 for i in range(2, n+1, 2)])