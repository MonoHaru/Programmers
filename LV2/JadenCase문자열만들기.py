# LV2 - JadenCase 문자열 만들기 문제의 해답
def solution(s):
    JC = s.lower().split(' ')
    answer = []
    for i in range(len(JC)):
        if JC[i] == '':
            answer.append('')
        else:
            answer.append(JC[i][0].upper() + JC[i][1:].lower())
    return " ".join(answer)