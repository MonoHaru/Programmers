# LV0 - qr code 문제의 해답
def solution(q, r, code):
    """
    :param q: int
    :param r: int
    :param code: str
    :return: str
    """
    return code[r::q]

print(solution(3, 1, "qjnwezgrpirldywt"))  # "jerry"
print(solution(1, 0, "programmers"))  # 	"programmers"