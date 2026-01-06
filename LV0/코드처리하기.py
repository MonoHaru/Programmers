# LV0 - 코드 처리하기 문제의 해답
def solution(code):
    return ''.join(code.split('1'))[::2] or 'EMPTY'
