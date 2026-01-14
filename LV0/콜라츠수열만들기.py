# LV0 - 콜라츠 수열 만들기 문제의 해답
def solution(n):
    answer = [n]
    while True:
        if n % 2 == 0:
            n /= 2
        else:
            n = 3 * n + 1
        answer.append(n)
        if n == 1:
            break 
    return answer