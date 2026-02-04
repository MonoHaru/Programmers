# LV2 - 괄호 회전하기 문제의 해답
def solution(s):
    """
    :param s: str
    :return: int
    """
    count = 0
    for i in range(len(s)):
        stack = []
        for brk in s:
            if not stack:
                stack.append(brk)
                continue
            if stack[-1] == '(' and brk == ')':
                stack.pop()
            elif stack[-1] == '{' and brk == '}':
                stack.pop()
            elif stack[-1] == '[' and brk == ']':
                stack.pop()
            else:
                stack.append(brk)
        if not stack:
            count += 1
        s = s[1:] + s[0]
    return count

print("[](){}")  # 3
print("}]()[{")  # 2
print("[)(]")  # 0
print("}}}")  # 0