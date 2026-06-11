# LV0 - OX퀴즈 문제의 해답
def solution(quiz: list) -> list:
    """공식 quiz의 값이 올바른지 확인합니다.

    Args:
        quiz (list[str]): 여러 개의 공식 리스트.

    Returns:
        list: 공식의 정답 유무    
    """
    answer = []
    for q in quiz:
        q = q.replace("=", "==")
        if eval(q):
            answer.append("O")
        else:
            answer.append("X")
    return answer

print(solution(["3 - 4 = -3", 
                "5 + 6 = 11"]))  # ["X", "O"]
print(solution(["19 - 6 = 13", 
                "5 + 66 = 71", 
                "5 - 15 = 63", 
                "3 - 1 = 2"]))   # ["O", "O", "X", "O"]