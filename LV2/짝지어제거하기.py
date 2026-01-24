# LV2 - 짝지어 제거하기 문제의 해답
def solution(s):
    """
    :param s: strs
    """
    stack = []
    for i in s:
        if not stack:
            stack.append(i)
        else:
            if stack[-1] == i:
                stack.pop()
            else:
                stack.append(i)
    return int(not stack)

print(solution("baabaa"))  # 1
print(solution("cdcd"))