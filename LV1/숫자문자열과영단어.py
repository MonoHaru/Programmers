# LV1 - 숫자 문자열과 영단어 문제의 해답
def solution(s):
    """
    :param s: str
    :return: int
    """
    num_dict = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9"
    }
    for word, digit in num_dict.items():
        s = s.replace(word, digit)
    return int(s)

print(solution("one4seveneight"))  # 1478
print(solution("23four5six7"))  # 234567
print(solution("2three45sixseven"))  # 234567
print(solution("123"))  # 123