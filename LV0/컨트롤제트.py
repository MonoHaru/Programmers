# LV0 - 컨트롤 제트 문제의 해답
def solution(s):
    """Z 이전에 나온 숫자를 제외한 총합을 구합니다.

    Args:
        s (str): 주어진 문자열.

    Returns:
        int: 총합    
    """
    answer = []
    for n in s.split():
        if n != "Z":
            answer.append(int(n))
        else:
            answer.pop()
    return sum(answer)

print(solution("1 2 Z 3"))      # 4
print(solution("10 20 30 40"))  # 100
print(solution("10 Z 20 Z 1"))  # 1
print(solution("10 Z 20 Z"))    # 0
print(solution("-1 -2 -3 Z"))   # -3