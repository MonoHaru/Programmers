# LV0 - 이어 붙인 수 문제의 해답
def solution(num_list):
    even, odd = '', ''
    for n in num_list:
        if n % 2 == 0:
            odd += str(n)
        else:
            even += str(n)
    return int(odd) + int(even)