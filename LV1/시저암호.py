# LV1 - 시저 암호 문제의 해답
def solution(s, n):
    """
    :param s: str
    :param n: int
    :return: str
    """
    answer = ''
    for c in s:
        if c == ' ':
            answer += c
        elif c.isupper():
            answer += chr((ord(c) + n - ord('A')) % 26 + ord('A'))
        else:
            answer += chr((ord(c) + n - ord('a')) % 26 + ord('a'))
    return answer

print(solution("AB", 1))  # "BC"
print(solution("z", 1))  # "a"
print(solution("a B z", 4))  # "e F d"