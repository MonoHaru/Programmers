# LV0 - 문자열 섞기 문제의 해답
def solution(str1, str2):
    return ''.join([str1[i] + str2[i] for i in range(len(str1))])