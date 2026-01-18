# LV2 - 이진 변환 반복하기 문제의 해답
def solution(s):
    cnt_loop = 0
    cnt_0 = 0
    while s != '1':
        cnt_0 += s.count('0')
        s = bin(s.count('1'))[2:]
        cnt_loop += 1
    return [cnt_loop, cnt_0]
    