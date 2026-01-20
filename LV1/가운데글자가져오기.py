# LV1 - 가운데 글자 가져오기 문제의 해답
def solution(s):
    half_len = len(s) // 2
    return s[half_len] if len(s) % 2 else s[half_len - 1: half_len + 1]

print(solution("abcde"))  # "c"
print(solution("qwer"))  # "we"