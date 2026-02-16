# LV1 - 가장 가까운 같은 글자 문제의 해답
def solution(s):
    """
    :param s: str
    return: list
    """
    tmp = dict()
    ans = []
    for i, c in enumerate(s):
        if c not in tmp.keys():
            ans.append(-1)
        else:
            ans.append(i - tmp[c])
        tmp[c] = i
    return ans

print(solution("banana"))  # [-1, -1, -1, 2, 2, 2]
print(solution("foobar"))  # [-1, -1, 1, -1, -1, -1]