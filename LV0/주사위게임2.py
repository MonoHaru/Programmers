# LV0 - 주사위 게임 2 문제의 해답
def solution(a, b, c):
    key = len(set([a, b, c]))
    if key == 1:
        return 27 * a * a ** 2 * a ** 3
    elif key == 2:
        return (a + b + c) * (a ** 2 + b ** 2 + c ** 2)
    else:
         return a + b + c