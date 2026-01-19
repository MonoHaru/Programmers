# LV2 - 숫자의 표현 문제의 해답
def solution(n):
    cnt = 0
    for i in range(1, n + 1):
        sum_ = 0
        while (sum_ < n):
            sum_ += i
            i += 1
        if sum_ == n:
            cnt += 1
    return cnt

print(solution(15))