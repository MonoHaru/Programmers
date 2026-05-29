# LV0 - 가위 바위 보 문제의 해답
def solution(rsp: str) -> str:
    """가위 바위 보를 이기기 위한 정답을 찾습니다.

    Args:
        rsp (str): 주어진 가위 바위 보 순서.

    Returns:
        str: 이기는 정답.
    """
    answer = ''
    for w in rsp:
        if w == "2":
            answer += "0"
        elif w == "0":
            answer += "5"
        else:
            answer += "2"
    return answer

print(solution("2"))    # "0"
print(solution("205"))  # "052"