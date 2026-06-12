# LV0 - 잘라서 배열로 저장하기 문제의 해답
def solution(my_str: str, n: int) -> list:
    """주어진 문자열 my_str을 정수 n만큼 자릅니다.

    Args:
        my_str (str): 주어진 문자열.
        n (int): 자르는 간격.

    Returns:
        list[str]: 잘려진 문자열 리스트.    
    """
    answer = []
    for i in range(0, len(my_str), n):
        answer.append(my_str[i : i + n])
    return answer

print(solution("abc1Addfggg4556b", 6))  # ["abc1Ad", "dfggg4", "556b"]
print(solution("abcdef123", 3))         # ["abc", "def", "123"]