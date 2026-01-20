# LV2 - 다음 큰 숫자 문제의 해답
def solution(n):
    """
    :param n: int -> 자연수
    
    :retrun: n의 2진수에서 '1' 갯수가 같은 n보다 큰 수
    """
    bin_n = bin(n)[2:].count('1')

    while True:
        n += 1
        if bin_n ==bin(n)[2:].count('1'):
            break

    return n

print(solution(78))  # 83
print(solution(15))  # 23