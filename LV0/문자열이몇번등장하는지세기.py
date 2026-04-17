# LV0 - 문자열이 몇 번 등장하는지 세기
def solution(myString, pat):
    """
    :param myString: str
    :param pat: str
    :return: int
    """
    ans = 0
    for i in range(len(myString) - len(pat) + 1):
        if myString[i:].startswith(pat):
            ans += 1
    return ans

print(solution("banana", "ana"))  # 2
print(solution("aaaa", "aa"))  # 3