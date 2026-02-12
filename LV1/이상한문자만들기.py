# LV1 - 이상한 문제 만들기 문제의 해답
def solution(s):
    """
    :param s: str
    :return: str
    """
    ans = []
    k = 0
    for ch in s:
        if ch == ' ':
            ans.append(' ')
            k = 0
        else:
            ans.append(ch.upper() if k % 2 == 0 else ch.lower())
            k += 1
    return ''.join(ans)

print(solution("try hello world"))  # "TrY HeLlO WoRlD"